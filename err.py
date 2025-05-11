import maliang
from maliang import theme
from loguru import logger
import webbrowser


def show_error(message, level):
    """显示错误信息"""
    logger.error("调用函数 show_error")

    error = maliang.Tk(size=(600, 400), icon="./img/EECT_logo.ico")
    error.center()
    error.title("EECT错误")
    error.resizable(False, False)
    theme.customize_window(error, disable_maximize_button=True, disable_minimize_button=True)
    error.topmost(True)

    error_cv = maliang.Canvas(error, auto_zoom=False)
    error_cv.place(width=600, height=400)
    error_title = maliang.Text(error_cv, (5, 10), text="EECT出现了一些错误", fontsize=24)
    error_text = maliang.Text(error_cv, (5, 60), text=message, fontsize=14, family="Microsoft Yahei UI")
    tips = maliang.Text(error_cv, (5, 300), text="请尝试重新启动程序或者忽略错误（如果不影响使用的话）。\n如果你认为这是一个bug，那么请点击“反馈问题”", fontsize=16)

    if level == 1:
        ignore = maliang.Button(error_cv, (280, 350), text="忽略错误", command=lambda: error.destroy())
        issue = maliang.Button(error_cv, (390, 350), text="反馈问题", command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/issues"))
        close = maliang.Button(error_cv, (500, 350), text="关闭程序", command=lambda: exit(1))
    else:
        ignore = maliang.Button(error_cv, (390, 350), text="忽略错误", command=lambda: error.destroy())
        issue = maliang.Button(error_cv, (500, 350), text="反馈问题", command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/issues"))

    error.mainloop()


if __name__ == "__main__":
    show_error("这是一个错误信息", 0)
    show_error("这是一个严重错误信息", 1)
