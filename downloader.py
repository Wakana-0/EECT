import requests
import os
import maliang

# import json #用于加载配置文件
# import tomllib #用于加载配置文件
# TODO: 增加配置文件功能

from tqdm import tqdm
from loguru import logger

# 获取当前用户的“下载”文件夹路径
def get_download_folder() -> str:
    return os.path.join(os.path.expanduser("~"), "Downloads")

# 打开下载文件夹
def open_explorer(path):
    os.startfile(path)

# 配置文件字典
config = {
    "download_folder": get_download_folder()  # 默认存放位置为“下载”文件夹
}

# 文件下载并显示进度条
def download_file(file_url, file_path):
    '''下载器核心'''
    try:
        response = requests.get(file_url, stream=True, timeout=60)  # 设置超时
        response.raise_for_status()  # 如果响应状态码不是 200，会抛出异常

        # 获取 Content-Length 或使用未知大小
        total_size = response.headers.get("content-length")
        if total_size is None:
            logger.warning("无法获取文件大小，下载可能会比较慢。")
            total_size = 0  # 设置为 0，下载时不会有进度条，直到下载完成

        total_size = int(total_size) if total_size else 0

        block_size = 1024  # 每次下载的块大小
        progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

        # 预留图形界面进度条显示
        # TODO: 增加图形界面进度条显示
        # maliang.ProgressBar(cv, (10, 10)).set(0) # 设置进度条起始位置 # 修改点：cv

        with open(file_path, "wb") as f:
            for data in response.iter_content(block_size):

                # 预留图形界面进度条显示
                # maliang.ProgressBar(cv, (10, 10)).set(len(data/block_size)) # 更新进度条进度 # 修改点：cv

                progress_bar.update(len(data))
                f.write(data) # 写入文件

        progress_bar.close()
        open_explorer(config["download_folder"])
        logger.info("文件下载完成")

    except requests.exceptions.Timeout:
        logger.error("下载超时，请检查网络连接或稍后重试。")
    except requests.exceptions.RequestException as e:
        logger.error(f"请求失败: {e}")
    except Exception as e:
        logger.error(f"下载过程中发生错误: {e}")

# 获取文件路径
def get_file_path(config, file_url, custom_path=None):
    if custom_path:
        return os.path.join(config["download_folder"], custom_path)
    return os.path.join(config["download_folder"], os.path.basename(file_url))


if __name__ == "__main__":
    # 示例用法
    info = ["https://i0.hdslb.com/bfs/face/71865821cf7cd5aef5e4f59f682a705d69cdf72e.jpg@120w_120h_1c.avif",\
            ""
            ]
    download_file(info[0], get_file_path(config, info[0], info[1]))
