import maliang
from maliang import theme, animation
from loguru import logger





def main_window():
    logger.info("创建窗口 root")
    root = maliang.Tk(size=(650, 450), icon="./img/EECT_logo.ico")
    root.center()
    root_cv = maliang.Canvas(root, auto_zoom=False)
    root_cv.place(width=650, height=450)
    root.title("EECT设置")
    root.resizable(False, False)
    settings_home(root_cv)
    root.mainloop()


def settings_home(cv):
    logger.info("设置主页")
    cv.clear()
    title = maliang.Text(cv, (270, 20), text="EECT设置", fontsize=26)
