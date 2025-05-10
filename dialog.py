import maliang
import webbrowser
import update
from tkinter import messagebox
from loguru import logger

# 错误信息弹窗
def ErrorDialog(window: maliang.Tk, error_message, title="错误信息") -> None:
    # 日志记录 & 窗口创建
    logger.info("调用 ErrorDialog 函数")
    logger.info("创建 ErrorDialog 窗口")
    error_dialog = maliang.Toplevel(window, size=(550, 400), icon="./img/EECT_logo.ico")
    error_dialog.center()
    error_dialog_cv = maliang.Canvas(error_dialog, auto_zoom=False)
    error_dialog_cv.place(width=584, height=445)
    error_dialog.title(title)
    error_dialog.resizable(False, False)

    # 错误信息标签
    error_text = maliang.Text(error_dialog_cv, (200, 5), text="哎呀，出错了！")
    error_message_label = maliang.Label(error_dialog_cv, (50, 50), text=f"                                              错误信息 | Error Message:                                                \n\n{error_message}", fontsize=12)

    # 关闭错误提示弹窗
    close_button = maliang.Button(error_dialog_cv, (135, 350), text="忽略错误", command=lambda: error_dialog.destroy())

    # 反馈按钮
    feedback_button = maliang.Button(error_dialog_cv, (300, 350), text="反馈问题", command=lambda: webbrowser.open("https://github.com/EECT/EECT/issues/new"))

if   __name__ == "__main__":
    pass