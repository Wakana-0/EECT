# https://github.com/EECT/EECT
import maliang
from maliang import theme
from tkinter import messagebox
import os
import datetime
from loguru import logger
import traceback

import requests
import psutil
import tomli_w
from packaging import version


version = 1


# 创建logs目录，如果不存在
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期和时间yyyy-mm-dd HH:MM:SS
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H`%M`%S")
# 设置日志文件名为当前日期和时间
log_file_name = f"{time_now}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# 配置日志
logger.add(log_file_path, level='DEBUG', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {module} | {message}')

logger.info("EECT启动")


def update_exe():
    try:
        os.startfile(".\\EECT-Update.exe")
    except FileNotFoundError:
        messagebox.showerror("组件错误", "无法打开“EECT更新组件”。\n此EECT没有附带“EECT更新组件” (EECT-Update.exe)。")


logger.info("导入核心模块")
import core
logger.info("导入基本模块")
import err

logger.info("检查核心版本")
if core.version() < 1:
    logger.error(f"核心版本过低，无法继续运行。当前核心版本: {core.version()}, 应用程序支持的最低版本: 1")
    err.show_error(f"核心版本过低，应用程序不支持此核心，请 更新 或 下载最新版本 的EECT解决此问题。\n核心版本: {core.version()}\n应用程序支持的最低版本: 1\n\n操作建议：更新或下载最新版本的EECT、关闭程序。", 1)
    exit(0)

logger.info("core")
core.mian()

'''
logger.info("创建窗口 root")
size = 600, 400
toplevel_size = 430, 350
root = maliang.Tk(size=size, icon="./img/EECT_logo.ico")
cv = maliang.Canvas(root, auto_zoom=True)
cv.place(width=600, height=400)
root.center()
root.title("EECT")
root.resizable(False, False)
root.at_exit(command=lambda: EECT_exit())
logger.info("设置颜色模式")
color_modes = {"0": "system", "1": "dark", "2": "light"}
theme.set_color_mode(color_modes[str(settings.get_value("appearance.color_mode"))])    # type: ignore

if ExperienceTheFeatures:
    logger.info("EECT已启用体验功能")
    root.title("EECT - 已启用体验功能")


# TODO: 重构 重构 重构 重构 重构……


def EECT_exit():
    logger.info("调用 EECT_exit 函数")
    logger.info("EECT退出")


def About():
    logger.info("调用 About 函数")
    logger.info("创建窗口 About")
    About = maliang.Toplevel(root, size=(650, 480), icon="./img/EECT_logo.ico")
    About.center()
    About_cv = maliang.Canvas(About, auto_zoom=False)
    About_cv.place(width=500, height=480, x=0, y=0)
    About_sidebar_cv = maliang.Canvas(About, auto_zoom=False)
    About_sidebar_cv.place(width=150, height=480, x=500, y=0)
    About.title("关于EECT")
    About.resizable(False, False)
    # EECT_logo = maliang.Image(About_cv, (20, 15), image=maliang.PhotoImage(file="./EECT_icon.png").resize(60, 60))
    About_title = maliang.Text(About_cv, (20, 20), text="EECT", fontsize=40)
    About_text = maliang.Text(About_cv, (20, 100), text=f"Version：{current_version}\nVersion code：{current_version_code}")
    update = maliang.Button(About_cv, (20, 165), text="检查更新", command=about.pull_up_the_update)
    EECT__update = maliang.Button(About_cv, (20, 225), text="启动“EECT更新组件”", command=update_exe)

    About_sidebar_text = maliang.Text(About_sidebar_cv, (0, 20), text="更多信息∨", fontsize=20)
    List_of_developers = maliang.UnderlineButton(About_sidebar_cv, (0, 70), text="贡献者名单", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/graphs/contributors"))
    thanks = maliang.UnderlineButton(About_sidebar_cv, (0, 100), text="鸣谢", fontsize=16, command=lambda: about.thanks(About))
    go_github = maliang.UnderlineButton(About_sidebar_cv, (0, 130), text="前往此项目仓库", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT"))
    issues = maliang.UnderlineButton(About_sidebar_cv, (0, 160), text="意见反馈", fontsize=16, command=lambda: webbrowser.open_new("https://github.com/EECT/EECT/issues"))
    open_source_license = maliang.UnderlineButton(About_sidebar_cv, (0, 190), text="开放源代码许可", fontsize=16, command=lambda: about.open_source_license(About))
    free_software_statement = maliang.UnderlineButton(About_sidebar_cv, (0, 220), text="免费软件声明", fontsize=16, command=lambda: about.free_software_statement(About))
    c = maliang.Label(About_cv, (20, 430), text="Copyright © 2025 EECT Team, All Rights Reserved.", fontsize=12)


def auto_shutdown():
    logger.info("调用 auto_shutdown 函数")
    logger.info("创建窗口 auto_shutdown_window")
    auto_shutdown_window = maliang.Toplevel(root, size=(400, 250), icon="./img/EECT_logo.ico")
    auto_shutdown_window.center()
    auto_shutdown_window_cv = maliang.Canvas(auto_shutdown_window, auto_zoom=False)
    auto_shutdown_window_cv.place(width=400, height=300)
    auto_shutdown_window.title("EECT - 设置定时关机")
    theme.customize_window(auto_shutdown_window, disable_maximize_button=True, disable_minimize_button=True)

    # 创建文本框和按钮
    shutdown_time_entry = maliang.InputBox(auto_shutdown_window_cv, (50, 20), (90, 40))
    shutdown_time_entry.insert(0, '60')  # 默认值为60秒

    shutdown_button = maliang.Button(auto_shutdown_window_cv, (150, 20), text='在设定的时间后关机', command=lambda: shutdown.set_shutdown_time(shutdown_time_entry))

    restart_time_entry = maliang.InputBox(auto_shutdown_window_cv, (50, 80), (90, 40))
    restart_time_entry.insert(0, '60')  # 默认值为60秒

    restart_button = maliang.Button(auto_shutdown_window_cv, (150, 80), text='在设定的时间后重启', command=lambda: shutdown.set_restart_time(restart_time_entry))

    cancel_button = maliang.Button(auto_shutdown_window_cv, (120, 140), text='取消关机或重启', command=shutdown.set_cancel_shutdown)

    tip = maliang.Label(auto_shutdown_window_cv, (35, 200), fontsize=12, text="Tips: 你也可以在cmd输入 shutdown /s /t [秒数] 定时关机")


def Windows_tools_toplevel():
    logger.info("调用 Windows_tools_toplevel 函数")
    logger.info("创建窗口 windows_tools_window")
    windows_tools_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    windows_tools_window.center()
    windows_tools_window_cv = maliang.Canvas(windows_tools_window, auto_zoom=False)
    windows_tools_window_cv.place(width=400, height=350)
    windows_tools_window.title("EECT - Windows工具")
    windows_tools_window.resizable(False, False)
    theme.customize_window(windows_tools_window, disable_maximize_button=True, disable_minimize_button=True)

    warning = maliang.Label(windows_tools_window_cv, (10, 20), fontsize=12, text="tips: 带有*的工具务必在专业指导下使用！")
    windows_reg = maliang.Button(windows_tools_window_cv, (10, 70), text='*注册表编辑器', command=lambda: os.system("start regedit"))
    windows_gpedit = maliang.Button(windows_tools_window_cv, (170, 70), text='*组策略编辑器',command=lambda: os.system("start gpedit.msc"))
    windows_cleanmgr = maliang.Button(windows_tools_window_cv, (10, 120), text='磁盘清理', command=lambda: os.system("start cleanmgr"))
    windows_compmgmt = maliang.Button(windows_tools_window_cv, (120, 120), text='*计算机管理', command=lambda: os.system("start compmgmt.msc"))
    windows_taskschd = maliang.Button(windows_tools_window_cv, (260, 120), text='任务计划程序', command=lambda: os.system("start taskschd.msc"))
    windows_df = maliang.Button(windows_tools_window_cv, (10, 170), text='*高级安全 Windows Defender 防火墙', command=lambda: os.system("start WF.msc"))
    more_tools = maliang.Button(windows_tools_window_cv, (10, 290), text='*更多高级工具', command=lambda: os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools"))


def find_games_toplevel():
    logger.info("调用 find_games_toplevel 函数")
    logger.info("创建窗口 find_games_toplevel")
    find_games_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    find_games_window.center()
    find_games_window_cv = maliang.Canvas(find_games_window, auto_zoom=False)
    find_games_window_cv.place(width=400, height=350)
    find_games_window.title("EECT - 查找电脑上的游戏")
    find_games_window.resizable(False, False)
    theme.customize_window(find_games_window, disable_maximize_button=True, disable_minimize_button=True)


    def find_games_window_def(root):
        logger.info("调用 find_games_window_def 函数")
        logger.info("创建窗口 find_games_windows")
        find_games_windows = maliang.Toplevel(find_games_window, size=(250, 70), title="正在查找……")
        find_games_windows.toolwindow(True)
        find_games_windows.center()
        find_games_windows_cv = maliang.Canvas(find_games_windows, auto_zoom=False)
        find_games_windows_cv.place(width=400, height=350)

        find_spinner = maliang.Spinner(find_games_windows_cv, (10, 15), mode="indeterminate")
        finding_text = maliang.Text(find_games_windows_cv, (55, 10), text=f"正在扫描{root}，请稍后……\n具体耗时由文件数量决定", fontsize=14)

        data = FindGames.find_games(root)

        if not Cache:
            logger.info("缓存被禁用")
            finding_text.destroy()
            find_spinner = maliang.Spinner(find_games_windows_cv, (10, 15), mode="indeterminate")
            finding_text = maliang.Text(find_games_windows_cv, (55, 10), text=f"扫描失败\n当前配置不允许使用缓存。\n因为 Cache={Cache}", fontsize=14)
            messagebox.showerror("功能被锁定", "当前配置不允许使用缓存相关功能。")
            find_games_windows.topmost(True)
            return

        # 获取当前时间
        logger.info("获取当前时间")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
        logger.info(f"当前时间：{current_time}")

        logger.info("缓存数据")
        try:
            with open("./cache/cache", "w") as f:
                f.write("")
        except FileNotFoundError as em:
            logger.info("缓存文件不存在，创建缓存目录")
            os.makedirs("./cache")
            with open("./cache/cache", "w") as f:
                f.write("")

        logger.info(f"写入缓存数据: ./cache/查找游戏-{current_time}.txt")
        with open(f"./cache/查找游戏-{current_time}.txt", "w", encoding="utf-8") as f:
            f.write("查找游戏结果：\n")
            for game_name, game_path in data:
                f.write(f"{game_name}: {game_path}\n")
                logger.info("完成本次查找")

        find_games_windows_cv.destroy()
        find_games_windows_cv = maliang.Canvas(find_games_windows, auto_zoom=False)
        find_games_windows_cv.place(width=400, height=350)
        button = maliang.Button(find_games_windows_cv, (10, 10), text="查看结果", command=lambda: os.startfile(os.path.abspath(f"./cache/查找游戏-{current_time}.txt")))



    find_games_text = maliang.Text(find_games_window_cv, (20, 20), text="在以下分区查找游戏【如：D（D盘）】：", fontsize=18)
    find_games_entry = maliang.InputBox(find_games_window_cv, (20, 60), (90, 40))
    find_games_button = maliang.Button(find_games_window_cv, (150, 60), text="查找", command=lambda: find_games_window_def(find_games_entry.get()))
    find_games_label = maliang.Label(find_games_window_cv, (65, 260), text="注意：\n查找结果仅供参考，并非100%准确！\n如果找出游戏，请前往对应目录检查。", fontsize=14)


def software_recommendations_toplevel():
    logger.info("调用 software_recommendations_toplevel 函数")
    logger.info("创建窗口 software_recommendations_window")
    software_recommendations_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    software_recommendations_window.center()
    software_recommendations_window_cv = maliang.Canvas(software_recommendations_window, auto_zoom=False)
    software_recommendations_window_cv.place(width=400, height=350)
    software_recommendations_window.title("EECT - 软件推荐")
    software_recommendations_window.resizable(False, False)
    theme.customize_window(software_recommendations_window, disable_maximize_button=True, disable_minimize_button=True)


def taskbar():
    logger.info("调用 taskbar 函数")
    if not UseRegistry:
        logger.info("注册表相关功能被禁用")
        messagebox.showerror("功能被锁定", "当前配置不允许使用注册表相关功能。")
        return
    logger.info("创建窗口 taskbar_window")
    taskbar_window = maliang.Toplevel(root, size=toplevel_size, icon="./img/EECT_logo.ico")
    taskbar_window.center()
    taskbar_window_cv = maliang.Canvas(taskbar_window, auto_zoom=False)
    taskbar_window_cv.place(width=450, height=350)
    taskbar_window.title("EECT - 设置任务栏")
    taskbar_window.resizable(False, False)
    theme.customize_window(taskbar_window, disable_maximize_button=True, disable_minimize_button=True)

    show_seconds = maliang.Button(taskbar_window_cv, (10, 20), text='在任务栏上显示秒', command=lambda: reg.show_seconds_in_system_clock(1))
    hide_seconds = maliang.Button(taskbar_window_cv, (200, 20), text='在任务栏上隐藏秒', command=lambda: reg.show_seconds_in_system_clock(0))

    show_weekday = maliang.Button(taskbar_window_cv, (10, 70), text='`在任务栏上显示星期', command=lambda: reg.show_weekday_in_taskbar(1))
    hide_weekday = maliang.Button(taskbar_window_cv, (220, 70), text='`在任务栏上隐藏星期', command=lambda: reg.show_weekday_in_taskbar(0))

    tips = maliang.Label(taskbar_window_cv, (10, 250), text="带`的功能有点问题，请谨慎使用。", fontsize=14)

    restart_explorer = maliang.Button(taskbar_window_cv, (10, 300), text='重启资源管理器', command=lambda: os.system("taskkill /f /im explorer.exe & start explorer.exe"))


logger.info("创建窗口 root 上的按钮")
home_text = maliang.Text(cv, (20, 20), text="“实用”小工具", fontsize=16)
home_button1 = maliang.Button(cv, (20, 60), text="定时关机", command=auto_shutdown)
home_button2 = maliang.Button(cv, (130, 60), text="查找电脑上的游戏", command=find_games_toplevel)
windows_tools_text = maliang.Text(cv, (20, 120), text="Windows工具 ∨", fontsize=16)
home_button3 = maliang.Button(cv, (20, 160), text="Windows工具", command=Windows_tools_toplevel)
home_button6 = maliang.Button(cv, (180, 160), text="设置任务栏", command=taskbar)

if ExperienceTheFeatures:
    software_recommendations_text = maliang.Text(cv, (20, 220), text="其他 ∨", fontsize=16)
    home_button4 = maliang.Button(cv, (20, 260), text="软件推荐`", command=software_recommendations_toplevel)

home_button5 = maliang.Button(cv, (20, 355), text="    关于    ", command=About)
settings_button = maliang.Button(cv, (130, 355), text="设置", command=lambda: settingsGUI.main_window(1, root))


beta_tips = maliang.Label(cv, (423, 350), text="你正在使用的是EECT的Beta版本！\nVersion: 1.1.0.0-b1 (250520)", fontsize=10)

dialog.tips(root, "Tips!", "Beta版本提醒", "当前正在使用的EECT是测试版，程序稳定性和功能完整性\n欠缺，不建议将此版本当作正式版使用。")


logger.info("EECT准备就绪，进入主循环")
root.mainloop()'''
