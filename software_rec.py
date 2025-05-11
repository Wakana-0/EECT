import maliang
from maliang import theme
from loguru import logger
import webbrowser
import ctypes


def software_rec():
    """软件推荐"""
    logger.info("调用函数 software_rec")
    software = maliang.Tk(size=(600, 400), icon="./img/EECT_logo.ico")
    software.center()
    software.title("EECT软件推荐")
    software.resizable(False, False)
    theme.customize_window(software, disable_maximize_button=True, disable_minimize_button=True)
    software.topmost(True)

    software_cv = maliang.Canvas(software, auto_zoom=False)
    software_cv.place(width=600, height=400)

    software_rec_category_list(software_cv)

    software.mainloop()


def software_rec_category_list(cv):
    cv.clear()
    title = maliang.Text(cv, (20, 20), text="软件推荐分类列表", fontsize=24)
    security_software = maliang.Button(cv, (20, 70), text="安全软件", command=lambda: security_software_rec())
    tool_software = maliang.Button(cv, (140, 70), text="工具软件", command=lambda: tool_software_rec())
    seewo_software = maliang.Button(cv, (260, 70), text="希沃软件")


    def security_software_rec():
        logger.info("调用函数 security_software_rec")
        cv.clear()
        title = maliang.Text(cv, (45, 0), text="安全软件推荐", fontsize=24)
        HuoRong = maliang.Button(cv, (20, 100), text="火绒安全软件", command=lambda: HuoRong_ask(cv))
        back_button = maliang.Button(cv, (0, 0), text="← ", command=lambda: software_rec_category_list(cv), fontsize=16)


    def HuoRong_ask(cv):
        logger.info("调用函数 HuoRong_ask")
        cv.clear()
        title = maliang.Text(cv, (20, 50), text="选择操作（火绒安全软件）", fontsize=26)
        text = maliang.Text(cv, (20, 100), text="你想要前往其官网还是下载安装程序？")
        install = maliang.Button(cv, (200, 170), text="→ 下载安装程序")
        web = maliang.Button(cv, (200, 220), text="→ 前往官网", command=lambda: webbrowser.open_new("https://www.huorong.cn/"))
        back = maliang.Button(cv, (0, 0), text="← ", command=lambda: security_software_rec(), fontsize=16)


    def tool_software_rec():
        logger.info("调用函数 tool_software_rec")
        cv.clear()
        title = maliang.Text(cv, (45, 0), text="工具软件推荐", fontsize=24)
        back_button = maliang.Button(cv, (0, 0), text="← ", command=lambda: software_rec_category_list(cv), fontsize=16)
        ClassWidgets = maliang.Button(cv, (20, 40), text="ClassWidgets", command=lambda: ClassWidgets_ask(cv))
        ClassIsland = maliang.Button(cv, (170, 40), text="ClassIsland", command=lambda: ClassIsland_ask(cv))



if __name__ == "__main__":
    software_rec()

