import os
from tkinter import messagebox


def msg(text: str) -> messagebox.askokcancel:  # 提示框
    result = messagebox.askokcancel('注意', text)
    return result


def shutdown(time: int):  # 关机
    os.system(f"shutdown /s /t {time}")


def restart(time: int):  # 重启
    os.system(f"shutdown /r /t {time}")


def cancel():  # 取消关机或重启
    os.system("shutdown /a")


def set_shutdown_time(entry) -> messagebox.askokcancel:
    time = entry.get()
    print(type(time))
    try:
        time = int(entry.get())
        if msg(f'确定要关机吗？关机将在{time}秒后执行。'):
            shutdown(time)
    except ValueError as f:
        messagebox.showerror('错误', f'你输入的值不正确\n\n{f}')


def set_restart_time(entry) -> messagebox.askokcancel:
    try:
        time = int(entry.get())
        if msg(f'确定要重启吗？重启将在{time}秒后执行。'):
            restart(time)
    except ValueError as f:
        messagebox.showerror('错误', f'你输入的值不正确\n\n{f}')


def set_cancel_shutdown():
    if msg(f'确定要取消已经设定的关机或重启任务吗？'):
        cancel()
