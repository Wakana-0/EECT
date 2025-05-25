import maliang
from maliang import animation
from loguru import logger
import os
import random
import tomllib

import update_settingsGUI
import shutdown
import reg


def menu_controls(value, cv):
    match value:
        case 0:
            auto_shutdown(cv)
        case 1:
            win_tools(cv)
        case 2:
            taskbar(cv)
        case 3:
            update_settingsGUI.settings_main(cv)


def main_window(window=0, top=None):
    if window == 0:
        logger.info("创建窗口 root")
        root = maliang.Tk(size=(750, 450), icon="./img/EECT_logo.ico")
        root.center()
        root_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv.place(width=200, height=450)
        root_cv.place(width=650, height=450, x=200)
        root.title("EECT")
        root.resizable(False, False)
        menu_bar(menu_cv, root_cv)
        auto_shutdown(root_cv)
        root.mainloop()
    else:
        logger.info("创建窗口 root")
        root = maliang.Toplevel(top, size=(850, 450), icon="./img/EECT_logo.ico")
        root.geometry(position=(root.winfo_screenwidth() // 2 - root.size[0] // 2, root.winfo_screenheight() // 2 - root.size[1] // 2))    # 居中窗口
        root_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv = maliang.Canvas(root, auto_zoom=False)
        menu_cv.place(width=200, height=450)
        root_cv.place(width=650, height=450, x=200)
        root.title("EECT")
        root.resizable(False, False)
        menu_bar(menu_cv, root_cv)
        auto_shutdown(root_cv)
        root.mainloop()


def menu_bar(cv, cv2):
    menu = maliang.SegmentedButton(cv, (0, 0), text=("定时关机               ", "Windows 工具      ", "修改任务栏            ", "更新    "), layout="vertical", default=0, command=lambda i:menu_controls(menu.get(), cv2))


def auto_shutdown(cv):
    logger.info("自动关机")
    cv.clear()

    cv.place(width=650, height=450, x=200, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    # 创建文本框和按钮
    shutdown_time_entry = maliang.InputBox(cv, (50, 20), (90, 40))
    shutdown_time_entry.insert(0, '60')  # 默认值为60秒

    maliang.Label(cv, (0, 0), text="标记点")

    shutdown_button = maliang.Button(cv, (150, 20), text='在设定的时间后关机', command=lambda: shutdown.set_shutdown_time(shutdown_time_entry))

    restart_time_entry = maliang.InputBox(cv, (50, 80), (90, 40))
    restart_time_entry.insert(0, '60')  # 默认值为60秒

    restart_button = maliang.Button(cv, (150, 80), text='在设定的时间后重启', command=lambda: shutdown.set_restart_time(restart_time_entry))

    cancel_button = maliang.Button(cv, (120, 140), text='取消关机或重启', command=shutdown.set_cancel_shutdown)

    tip = maliang.Label(cv, (35, 200), fontsize=12, text="Tips: 你也可以在cmd输入 shutdown /s /t [秒数] 定时关机")


def win_tools(cv):
    logger.info("Windows工具")
    cv.clear()

    cv.place(width=650, height=450, x=200, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    warning = maliang.Label(cv, (10, 20), fontsize=12, text="tips: 带有*的工具务必在专业指导下使用！")
    windows_reg = maliang.Button(cv, (10, 70), text='*注册表编辑器', command=lambda: os.system("start regedit"))
    windows_gpedit = maliang.Button(cv, (170, 70), text='*组策略编辑器', command=lambda: os.system("start gpedit.msc"))
    windows_cleanmgr = maliang.Button(cv, (10, 120), text='磁盘清理', command=lambda: os.system("start cleanmgr"))
    windows_compmgmt = maliang.Button(cv, (120, 120), text='*计算机管理', command=lambda: os.system("start compmgmt.msc"))
    windows_taskschd = maliang.Button(cv, (260, 120), text='任务计划程序', command=lambda: os.system("start taskschd.msc"))
    windows_df = maliang.Button(cv, (10, 170), text='*高级安全 Windows Defender 防火墙', command=lambda: os.system("start WF.msc"))
    more_tools = maliang.Button(cv, (10, 290), text='*更多高级工具', command=lambda: os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools"))


def taskbar(cv):
    logger.info("修改任务栏")
    cv.clear()

    cv.place(width=650, height=450, x=200, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    show_seconds = maliang.Button(cv, (10, 20), text='在任务栏上显示秒', command=lambda: reg.show_seconds_in_system_clock(1))
    hide_seconds = maliang.Button(cv, (200, 20), text='在任务栏上隐藏秒', command=lambda: reg.show_seconds_in_system_clock(0))

    show_weekday = maliang.Button(cv, (10, 70), text='`在任务栏上显示星期', command=lambda: reg.show_weekday_in_taskbar(1))
    hide_weekday = maliang.Button(cv, (220, 70), text='`在任务栏上隐藏星期', command=lambda: reg.show_weekday_in_taskbar(0))

    tips = maliang.Label(cv, (10, 250), text="带`的功能有点问题，请谨慎使用。", fontsize=14)

    restart_explorer = maliang.Button(cv, (10, 300), text='重启资源管理器', command=lambda: os.system("taskkill /f /im explorer.exe & start explorer.exe"))


if __name__ == "__main__":
    main_window(0)
