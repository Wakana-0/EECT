import maliang
from maliang import animation, theme
from loguru import logger
import os
import random
import tomllib
import webbrowser

import shutdown
import reg
import settings
import settingsGUI
from update import check_version
import about
import dialog
import core


def menu_controls(value, cv):
    match value:
        case 0:
            auto_shutdown(cv)
        case 1:
            win_tools(cv)
        case 2:
            taskbar(cv)
        case 3:
            system_info(cv)


def main_window():
    theme.set_color_mode(settings.get_color_mode())
    logger.info("创建窗口 root")
    root = maliang.Tk(size=(750, 450), icon="./img/EECT_logo.ico")
    root.center()
    root_cv = maliang.Canvas(root, auto_zoom=False)
    menu_cv = maliang.Canvas(root, auto_zoom=False)
    menu_cv.place(width=200, height=450)
    root_cv.place(width=650, height=450, x=200)
    root.title(f"EECT    -{core.名人名言()}-")
    root.resizable(False, False)
    menu_bar(menu_cv, root_cv, root)
    auto_shutdown(root_cv)
    dialog.tips(root, "Tips!", "Beta版本提醒", "当前正在使用的EECT是测试版，程序稳定性和功能完整性\n欠缺，不建议将此版本当作正式版使用。")
    root.mainloop()


def menu_bar(cv, cv2, window):
    menu = maliang.SegmentedButton(cv, (0, 0), text=("定时关机               ", "Windows 工具      ", "修改任务栏            ", "系统信息               "), layout="vertical", default=0, command=lambda i:menu_controls(menu.get(), cv2))
    about_button = maliang.Button(cv, (0, 358), text="            关于            ", command=lambda: About(cv2))
    settings_button = maliang.Button(cv, (0, 400), text="            设置            ", command=lambda: settingsGUI.main_window(1, window))


def About(cv):
    logger.info("关于界面")
    cv.clear()

    cv.place(width=650, height=450, x=200, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)
    
    # EECT_logo = maliang.Image(cv, (20, 15), image=maliang.PhotoImage(file="./EECT_icon.png").resize(60, 60))
    About_title = maliang.Text(cv, (20, 20), text="EECT", fontsize=40)
    About_text = maliang.Text(cv, (20, 100), text=f"Version：{check_version(1)}\nVersion code：{check_version(0)}")
    update = maliang.Button(cv, (20, 165), text="检查更新", command=about.pull_up_the_update)
    # EECT__update = maliang.Button(cv, (20, 225), text="启动“EECT更新组件”", command=update_exe)

    About_sidebar_text = maliang.Text(cv, (400, 20), text="更多信息∨", fontsize=20)
    List_of_developers = maliang.UnderlineButton(cv, (400, 70), text="贡献者名单", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/graphs/contributors"))
    thanks = maliang.UnderlineButton(cv, (400, 100), text="鸣谢", fontsize=16, command=lambda: about.thanks(About))
    go_github = maliang.UnderlineButton(cv, (400, 130), text="前往此项目仓库", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT"))
    issues = maliang.UnderlineButton(cv, (400, 160), text="意见反馈", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/issues"))
    open_source_license = maliang.UnderlineButton(cv, (400, 190), text="开放源代码许可", fontsize=16, command=lambda: about.open_source_license(About))
    free_software_statement = maliang.UnderlineButton(cv, (400, 220), text="免费软件声明", fontsize=16, command=lambda: about.free_software_statement(About))
    c = maliang.Label(cv, (20, 410), text="Copyright © 2025 EECT Team, All Rights Reserved.", fontsize=12)
    
    
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


def system_info(cv):
    logger.info("系统信息")
    cv.clear()
    wait = maliang.Label(cv, (20, 20), text="正在获取信息……")

    cv.place(width=650, height=450, x=200, y=40)
    animation.MoveTkWidget(cv, (0, -40), 200, fps=60).start(delay=50)

    wait.destroy()
    system = maliang.Text(cv, (20, 20), text=f"操作系统: {core.system_basic_information()[0]}\n版本: {core.system_basic_information()[1]}\n架构: {core.system_basic_information()[2]}", fontsize=16)
    cpu = maliang.Text(cv, (20, 100), text=f"CPU: {core.cpu_info()[0]}\n        {core.cpu_info()[1]}核{core.cpu_info()[2]}线程", fontsize=16)
    RAM = maliang.Text(cv, (20, 160), text=f"运行内存: {core.RAM_info():.1f}GB", fontsize=16)
    display = maliang.Text(cv, (20, 200), text=f"当前使用分辨率: {core.display_info()}", fontsize=16)


if __name__ == "__main__":
    main_window(0)
