import os
from tkinter import messagebox
from loguru import logger


def msg(text):  # 提示框
    logger.info("调用 msg 函数，传入参数：" + text)
    result = messagebox.askokcancel('注意', text)
    return result


def shutdown(time):  # 关机
    logger.info("调用 shutdown 函数")
    os.system(f"shutdown /s /t {time}")
    logger.info(f"设定了一个{time}秒的定时关机")


def restart(time):  # 重启
    logger.info("调用 restart 函数")
    os.system(f"shutdown /r /t {time}")
    logger.info(f"设定了一个{time}秒的定时重启")


def cancel():  # 取消关机或重启
    logger.info("调用 cancel 函数")
    os.system("shutdown /a")
    logger.info("取消了定时关机或重启")


def set_shutdown_time(entry):
    time = entry.get()
    print(type(time))
    try:
        time = int(entry.get())
        if msg(f'确定要关机吗？关机将在{time}秒后执行。'):
            shutdown(time)
    except ValueError as f:
        logger.error(f"输入的值不正确：{f}")
        messagebox.showerror('错误', f'你输入的值不正确\n\n{f}')


def set_restart_time(entry):
    try:
        time = int(entry.get())
        if msg(f'确定要重启吗？重启将在{time}秒后执行。'):
            restart(time)
    except ValueError as f:
        logger.error(f"输入的值不正确：{f}")
        messagebox.showerror('错误', f'你输入的值不正确\n\n{f}')


def set_cancel_shutdown():
    if msg(f'确定要取消已经设定的关机或重启任务吗？'):
        cancel()
