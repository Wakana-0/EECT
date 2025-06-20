import maliang
from maliang import theme, animation
from loguru import logger

import update_settings
import settings

config = None


def main_window():
    logger.info("创建窗口 root")
    root = maliang.Tk(size=(650, 450), icon="./img/EECT_logo.ico")
    root.center()
    root_cv = maliang.Canvas(root, auto_zoom=False)
    root_cv.place(width=650, height=450)
    root.title("更新设置")
    root.resizable(False, False)
    settings_main(root_cv)
    root.mainloop()


def settings_main(cv):
    logger.info("设置-更新")
    cv.clear()

    cv.place(width=650, height=450, x=100, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    title = maliang.Text(cv, (20, 20), text="更新设置", fontsize=26)

    update_channel_choose_text = maliang.Text(cv, (20, 80), text="更新频道选择")
    update_channel_choose = maliang.OptionButton(cv, (20, 120), text=("正式版（推荐，包含bug修复和新功能，稳定性高）", "测试版（包含最新bug修复或新功能，稳定性较低）"), default=int(update_settings.get_value("update_channel")))
    update_channel_choose.command = lambda event: update_settings.set_update_channel(update_channel_choose.get())

    download_source_choose_text = maliang.Text(cv, (20, 200), text="下载源选择（如果无法下载更新，请切换下载源）")
    download_source_choose = maliang.OptionButton(cv, (20, 240), text=("Github", "Proxy"), default=int(update_settings.get_value("download_source")))
    download_source_choose.command = lambda event: update_settings.set_download_source(download_source_choose.get())
