import maliang
from maliang import animation
from loguru import logger
import settings
import random
import tomllib

import update_settingsGUI


def menu_controls(value, cv):
    match value:
        case 0:
            settings_home(cv)
        case 1:
            settings_appearance(cv)
        case 2:
            settings_storage(cv)
        case 3:
            update_settingsGUI.settings_main(cv)


def main_window(window=0, top=None):
    if window == 0:
        logger.info("创建窗口 root")
        root = maliang.Tk(size=(750, 450), icon="./img/EECT_logo.ico")
        root.center()
        root_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv.place(width=100, height=450)
        root_cv.place(width=650, height=450, x=100)
        root.title("EECT设置")
        root.resizable(False, False)
        menu_bar(menu_cv, root_cv)
        settings_home(root_cv)
        root.mainloop()
    else:
        logger.info("创建窗口 root")
        root = maliang.Toplevel(top, size=(750, 450), icon="./img/EECT_logo.ico")
        root.geometry(position=(root.winfo_screenwidth() // 2 - root.size[0] // 2, root.winfo_screenheight() // 2 - root.size[1] // 2))    # 居中窗口
        root_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv.place(width=100, height=450)
        root_cv.place(width=650, height=450, x=100)
        root.title("EECT设置")
        root.resizable(False, False)
        menu_bar(menu_cv, root_cv)
        settings_home(root_cv)
        root.mainloop()


def menu_bar(cv, cv2):
    menu = maliang.SegmentedButton(cv, (0, 0), text=("主页    ", "外观    ", "存储    ", "更新    "), layout="vertical", default=0, command=lambda i:menu_controls(menu.get(), cv2))


def settings_home(cv):
    logger.info("设置主页")
    cv.clear()

    cv.place(width=650, height=450, x=100, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)
    title = maliang.Text(cv, (270, 20), text="EECT设置", fontsize=26)
    id = random.randint(1, 8)
    with open("./config/FamousQuotes.toml", 'rb') as f:
        famous_quotes = tomllib.load(f)
    text = famous_quotes[str(id)]
    Famous_quotes = maliang.Label(cv, (320, 80), text=text, fontsize=16, anchor="n")


def settings_appearance(cv):
    logger.info("设置-外观")
    cv.clear()

    cv.place(width=650, height=450, x=100, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    title = maliang.Text(cv, (20, 20), text="外观设置", fontsize=26)
    color_mode_text = maliang.Text(cv, (20, 90), text="设置颜色模式")
    color_mode = maliang.SegmentedButton(cv, (20, 130), text=("跟随系统", "深色", "浅色"), default=int(settings.get_value("appearance.color_mode")), command=lambda i: settings.set_color_mode(color_mode.get()))


def settings_storage(cv):
    logger.info("设置-存储")
    cv.clear()

    cv.place(width=650, height=450, x=100, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    title = maliang.Text(cv, (20, 20), text="存储设置（演示界面）", fontsize=26)
