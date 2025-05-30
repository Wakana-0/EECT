import maliang
from maliang import theme
import webbrowser
import update
from tkinter import messagebox
from loguru import logger
import winsound


# TODO: 完善错误信息弹窗
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


def tips(window, title_bar, title, text):   # 普通提示弹窗
    logger.info(f"传入参数：\n标题栏：{title_bar}\n标题：{title}\n文本：{text}")
    winsound.PlaySound("C:\\Windows\\Media\\Windows Background.wav", winsound.SND_ASYNC)  # 播放提示音
    tips = maliang.Toplevel(window, size=(450, 300), icon="./img/EECT_logo.ico", title=title_bar)
    tips.topmost(True)
    theme.customize_window(tips, disable_maximize_button=True, disable_minimize_button=True)
    tips.center()
    
    tips_cv = maliang.Canvas(tips, auto_zoom=False)
    tips_cv.place(width=450, height=300)

    img = maliang.Image(tips_cv, (15, 10), image=maliang.PhotoImage(file="./img/info.png").resize(45, 45))
    tips_title = maliang.Text(tips_cv, (70, 15), text=title, fontsize=24)
    tips_text = maliang.Text(tips_cv, (20, 60), text=text, fontsize=16)

    close = maliang.Button(tips_cv, (355, 250), text="  关 闭  ", command=lambda: tips.destroy())

    tips.mainloop()


if __name__ == "__main__":
    tips(None, "标题栏", "测试标题", "我仍感叹于世界之大\n也沉醉于儿时情话\n不剩真假 不做挣扎 无谓笑话\n我终将青春还给了她\n连同指尖弹出的盛夏\n心之所动 就随风去了\n以爱之名 你还愿意吗")
    