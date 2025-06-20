# https://github.com/EECT/EECT
import maliang
from maliang import theme
from tkinter import messagebox
import os
import datetime
from loguru import logger
import traceback

import requests
import certifi
import psutil
import tomli_w
from packaging import version
import wmi
import win10toast
from win10toast import ToastNotifier
import tkinter
from tkinter import ttk

import update

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


logger.info("导入核心模块")
import core
logger.info("导入基本模块")
import err

logger.info("检查核心版本")
if core.version() < 1:
    logger.error(f"核心版本过低，无法继续运行。当前核心版本: {core.version()}, 应用程序支持的最低版本: 1")
    err.show_error(f"核心版本过低，应用程序不支持此核心，请 更新 或 下载最新版本 的EECT解决此问题。\n核心版本: {core.version()}\n应用程序支持的最低版本: 1\n\n操作建议：更新或下载最新版本的EECT、关闭程序。", 1)
    exit(0)

logger.info("检查主程序是否满足核心最低版本要求")
if not core.version_verification(version):
    logger.error(f"主程序版本过低，不满足核心最低要求，无法继续运行。当前主程序版本: {version}")
    err.show_error(f"主程序版本过低，主程序不支持此核心，请 下载最新版本 的EECT解决此问题。\n主程序版本: {version}\n\n操作建议：下载最新版本的EECT、关闭程序。", 1)
    exit(1)


# 检查更新
try:
    ud_info = update.update()
    if ud_info[0]:
        # 初始化通知对象
        toaster = win10toast.ToastNotifier()

        # 发送基础通知
        toaster.show_toast(
            title="EECT更新",
            msg=f"当前使用的EECT不是最新的。\n最新版本：{ud_info[1]}，当前版本：{update.check_version(1)}\n\n转到“关于”了解详细信息。",
            duration=10,  # 显示时长（秒）
            threaded=True,  # 启用后台线程
            icon_path="./img/EECT_logo.ico"
        )
except Exception as e:
    # 初始化通知对象
    toaster = win10toast.ToastNotifier()

    # 发送基础通知
    toaster.show_toast(
        title="EECT更新 - 更新检查失败",
        msg=f"{e}",
        duration=10,  # 显示时长（秒）
        threaded=True,  # 启用后台线程
        icon_path="./img/EECT_logo.ico"
    )


logger.info("core")
core.mian()
