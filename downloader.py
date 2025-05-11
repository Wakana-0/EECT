import requests
import os
from tqdm import tqdm
from loguru import logger
import threading
from queue import Queue
import traceback
import err

# 全局变量，用于控制下载是否中断
download_interrupted = threading.Event()
wrote = 0
total_size = 0


def download_file(file_name, file_url, file_path, progress_queue=None):
    global wrote, total_size
    """
    下载文件并显示进度条（支持中断）

    :param file_name: 文件名
    :param file_url: 下载链接
    :param file_path: 保存路径
    :param progress_queue: 进度队列（可选）
    """
    try:
        response = requests.get(file_url, stream=True, timeout=60, verify=False)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        print(total_size)
        block_size = 1024
        wrote = 0

        # 创建缓存目录（如果不存在）
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        logger.info("开始下载文件...")
        with open(os.path.join(file_path, file_name), "wb") as file:
            with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
                for data in response.iter_content(block_size):
                    # 检查是否中断
                    if download_interrupted.is_set():
                        logger.info("下载已中断")
                        return

                    wrote += len(data)
                    file.write(data)
                    pbar.update(len(data))
                    if progress_queue:
                        progress_queue.put((wrote / total_size * 100) if total_size > 0 else 0)
                    if wrote >= total_size:
                        logger.info("文件下载完成")
                        return True

    except requests.exceptions.Timeout:
        logger.error(f"下载超时，{traceback.format_exc()}")
        err.show_error(traceback.format_exc(), 0)
        return False
    except requests.exceptions.RequestException:
        logger.error(f"请求失败: {traceback.format_exc()}")
        err.show_error(traceback.format_exc(), 0)
        return False
    except Exception:
        logger.error(f"下载过程中发生错误: {traceback.format_exc()}")
        err.show_error(traceback.format_exc(), 0)
        return False


def download_in_thread(file_name, file_url, file_path):
    """
    在单独线程中下载文件

    :param file_name: 文件名
    :param file_url: 下载链接
    :param file_path: 保存路径
    :return: 下载线程对象
    """
    progress_queue = Queue()
    thread = threading.Thread(
        target=download_file,
        args=(file_name, file_url, file_path, progress_queue)
    )
    thread.start()
    return thread


def stop_download():
    """
    强制中断下载（设置标志位）
    """
    logger.info("请求中断下载")
    download_interrupted.set()
    logger.info("下载中断标志已设置")


def get_download_progress():
    """
    获取当前下载进度

    :return: 下载进度（小数）
    """
    if total_size > 0:
        return wrote / total_size
    return 0


if __name__ == "__main__":
    # 示例：下载文件
    file_name = "EECT_1.0.0.1.250509.1.-windows-x64.zip"
    file_url = "https://github.com/EECT/EECT/releases/download/v1.0.0.1/EECT_1.0.0.1.250509.1.-windows-x64.zip"
    file_path = "./cache/download"

    # 确保下载目录存在
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # 在单独线程中下载文件
    download_thread = download_in_thread(file_name, file_url, file_path)

    download_thread.join()  # 等待线程结束
    print("程序结束")
