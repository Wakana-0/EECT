import maliang
from maliang import theme
from loguru import logger
import threading

import downloader
import update
import time
import err

# 全局变量，用于控制下载是否中断
download_interrupted = threading.Event()


def stop(cv, window):
    """停止下载"""
    logger.info("调用函数 stop")
    download_interrupted.set()
    downloader.stop_download()
    update_info(cv, window)


def get_progress_bar(progress_bar_name):
    """获取当前进度条进度"""
    return progress_bar_name.get()


def update_progress_bar(progress_bar_name, progress):
    """更新进度条"""
    while not progress_bar_name.get() >= 1 and not download_interrupted.is_set():
        if progress_bar_name.get() >= 1:
            logger.info("进度条已完成")
            return
        if download_interrupted.is_set():
            logger.info("下载已中断")
            return
        progress = downloader.get_download_progress()
        progress_bar_name.set(progress)
        time.sleep(0.01)


def update_progress_bar_threading(progress_bar_name, progress):
    """在单独线程中更新进度条"""
    logger.info("调用函数 update_progress_bar_threading")
    thread = threading.Thread(
        target=update_progress_bar,
        args=(progress_bar_name, progress)
    )
    thread.start()
    return thread


def update_window():
    logger.info("调用函数 update_window")
    logger.info("创建 update_window 窗口")
    update_window = maliang.Tk(size=(600, 400), icon="./img/EECT_logo.ico")
    update_window.center()
    update_window.title("EECT更新")
    update_window.resizable(False, False)
    theme.customize_window(update_window, hide_button="all")
    update_window.topmost(True)
    update_cv = maliang.Canvas(update_window, auto_zoom=False)
    update_cv.place(width=600, height=400)
    updateGUI(update_cv, update_window)
    update_window.mainloop()


def updateGUI(cv, window):
    logger.info("调用函数 updateGUI")
    cv.clear()
    title = maliang.Text(cv, (20, 20), text="EECT更新", fontsize=32)
    version = maliang.Text(cv, (20, 80), text="当前版本：%s\n版本码：%s" % (update.check_version(1), update.check_version(0)))
    cheek_update = maliang.Button(cv, (20, 160), text="检查更新", command=lambda: update_info(cv, window))
    close = maliang.Button(cv, (20, 210), text="关闭", command=lambda: window.destroy())


def update_info(cv, window):
    logger.info("调用函数 update_info")
    cv.clear()
    back = maliang.Button(cv, (0, 0), text="← ", command=lambda: updateGUI(cv, window), fontsize=16)
    cheek_version = update.update()
    update_text = maliang.Text(cv, (45, 0), text="EECT更新信息", fontsize=26)
    version_info = maliang.Text(cv, (20, 80), text=f"当前版本：{update.check_version(1)}\n版本码：{update.check_version(0)}\n\n最新版本：{cheek_version[1]}\n版本码：{cheek_version[2]}\n发布日期：{cheek_version[3]}\n更新日志：{cheek_version[4]}\n重要程度：{[cheek_version[5]]}", fontsize=14)
    if cheek_version[0]:
        logger.info("检测到新版本")
        compare = "有可用更新！"
        download = maliang.Button(cv, (20, 350), text="下载更新", command=lambda: download_update(cv, window, cheek_version[6], cheek_version[7]))
    else:
        logger.info("当前已是最新版本")
        compare = "当前已是最新版本！"
    update_text = maliang.Text(cv, (20, 50), text=compare)


def download_update(cv, window, name, url):
    logger.info("调用函数 download_update")
    cv.clear()
    wait = maliang.Spinner(cv, (150, 180), mode="indeterminate")
    update_text = maliang.Text(cv, (210, 180), text="正在下载更新，请稍等...")
    download_progress = maliang.ProgressBar(cv, (100, 220))
    update_progress_bar_threading(download_progress, downloader.get_download_progress())
    back = maliang.Button(cv, (240, 300), text="停止下载", command=lambda: stop(cv, window))
    downloader.download_in_thread(name, url, "./cache/download")



if __name__ == "__main__":
    update_window()
