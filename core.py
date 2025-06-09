import os

from loguru import logger
import tomllib
import traceback
import platform
import wmi
import ctypes
import random
import shutil
from tkinter import messagebox

logger.info("加载EECT核心必要模块")
import GUI
import err

_logs_path = "./logs"
build = 250610.1


def version():
    return 1


def build_version():
    return build


def version_verification(version):
    if version < 1:
        return False
    else:
        return True


def mian():
    read_config()
    GUI.main_window()


# -----配置文件/日志区-----

def read_config():    # 读取配置文件
    logger.info("EECT正在读取配置文件: ./config/config.toml")
    # 读取配置文件
    with open('./config/config.toml', 'rb') as f:
        config = tomllib.load(f)
        try:
            ExperienceTheFeatures = config['ExperienceTheFeatures']
            Cache = config['Cache']
            UseRegistry = config['UseRegistry']
        except KeyError as e:
            ExperienceTheFeatures = False
            err.show_error(traceback.format_exc(), 0)
            logger.error(f"读取配置文件时错误，堆栈信息：\n{traceback.format_exc()}")

    try:
        logger.info("EECT正在读取版本信息: ./config/version.toml")
        with open('./config/version.toml', 'rb') as f:
            version = tomllib.load(f)
        current_version = version['version']
        current_version_code = version['version_code']
    except FileNotFoundError as e:
        logger.error(f"EECT无法读取版本信息，堆栈信息：\n{traceback.format_exc()}")
        err.show_error(traceback.format_exc(), 0)
    except KeyError as e:
        logger.error(f"EECT无法读取版本信息，堆栈信息：\n{traceback.format_exc()}")
        err.show_error(traceback.format_exc(), 1)
        logger.info("程序退出")
        exit(0)


def delete_logs():
    try:
        logger.info("删除日志")
        logger.info("停止记录日志")
        logger.stop()
        shutil.rmtree(_logs_path)
        messagebox.showwarning("需要重新启动应用程序", "日志删除完成，需要重新启动程序。\n\n点击“确定”重新启动程序。")
        try:
            os.startfile("EECT.exe")
            exit(0)
        except FileNotFoundError:
            os.startfile("main.py")
            exit(0)
    except Exception:
        messagebox.showerror("错误", f"日志删除失败。\n\n{traceback.format_exc()}")
        logger.error(f"日志删除失败：{traceback.format_exc()}")


# -----系统信息区-----

def system_basic_information():
    return platform.system(), platform.version(), platform.machine()    # 返回 系统类型、版本、架构


def cpu_info():
    c = wmi.WMI()
    for proc in c.Win32_Processor():
        cpu_name = proc.Name
        cpu_cores = proc.NumberOfCores
        cpu_threads = proc.NumberOfLogicalProcessors

        return cpu_name, cpu_cores, cpu_threads    # 返回 CPU名称、物理核心数、逻辑线程数


def RAM_info():
    c = wmi.WMI()
    os_mem = c.Win32_OperatingSystem()[0]
    memory_size = int(os_mem.TotalVisibleMemorySize) / 1024 / 1024    # 总内存大小

    return memory_size    # 返回 总内存大小（GB）


def display_info():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)  # 获取屏幕宽度
    height = user32.GetSystemMetrics(1)  # 获取屏幕高度

    return f"{width}x{height}"    # 返回当前使用的屏幕分辨率（宽x高）


# -----名人名言-----

def 名人名言():    # 欸我去，def居然惊现中文字符😱！！！
    id = random.randint(1, 10)
    with open("./config/FamousQuotes.toml", 'rb') as f:
        famous_quotes = tomllib.load(f)
    text = famous_quotes[str(id)]
    return text


"""-----以下为测试代码-----"""


# noinspection PyMethodMayBeStatic
class CoreVersion:
    def version(self):
        return 1

    def core_build(self):
        return build

    def version_verification(self, version):
        if version < 1:
            return False
        else:
            return True


# noinspection PyMethodMayBeStatic
class Function:
    # -----配置文件/日志区-----

    def read_config(self):  # 读取配置文件
        logger.info("EECT正在读取配置文件: ./config/config.toml")
        # 读取配置文件
        with open('./config/config.toml', 'rb') as f:
            config = tomllib.load(f)
            try:
                ExperienceTheFeatures = config['ExperienceTheFeatures']
                Cache = config['Cache']
                UseRegistry = config['UseRegistry']
            except KeyError as e:
                ExperienceTheFeatures = False
                err.show_error(traceback.format_exc(), 0)
                logger.error(f"读取配置文件时错误，堆栈信息：\n{traceback.format_exc()}")

        try:
            logger.info("EECT正在读取版本信息: ./config/version.toml")
            with open('./config/version.toml', 'rb') as f:
                version = tomllib.load(f)
            current_version = version['version']
            current_version_code = version['version_code']
        except FileNotFoundError as e:
            logger.error(f"EECT无法读取版本信息，堆栈信息：\n{traceback.format_exc()}")
            err.show_error(traceback.format_exc(), 0)
        except KeyError as e:
            logger.error(f"EECT无法读取版本信息，堆栈信息：\n{traceback.format_exc()}")
            err.show_error(traceback.format_exc(), 1)
            logger.info("程序退出")
            exit(0)

    def delete_logs(self):
        try:
            logger.info("删除日志")
            logger.info("停止记录日志")
            logger.stop()
            shutil.rmtree(_logs_path)
            messagebox.showwarning("需要重新启动应用程序", "日志删除完成，需要重新启动程序。\n\n点击“确定”重新启动程序。")
            try:
                os.startfile("EECT.exe")
                exit(0)
            except FileNotFoundError:
                os.startfile("main.py")
                exit(0)
        except Exception:
            messagebox.showerror("错误", f"日志删除失败。\n\n{traceback.format_exc()}")
            logger.error(f"日志删除失败：{traceback.format_exc()}")

    # -----系统信息区-----

    def system_basic_information(self):
        return platform.system(), platform.version(), platform.machine()  # 返回 系统类型、版本、架构

    def cpu_info(self):
        c = wmi.WMI()
        for proc in c.Win32_Processor():
            cpu_name = proc.Name
            cpu_cores = proc.NumberOfCores
            cpu_threads = proc.NumberOfLogicalProcessors

            return cpu_name, cpu_cores, cpu_threads  # 返回 CPU名称、物理核心数、逻辑线程数

    def RAM_info(self):
        c = wmi.WMI()
        os_mem = c.Win32_OperatingSystem()[0]
        memory_size = int(os_mem.TotalVisibleMemorySize) / 1024 / 1024  # 总内存大小

        return memory_size  # 返回 总内存大小（GB）

    def display_info(self):
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)  # 获取屏幕宽度
        height = user32.GetSystemMetrics(1)  # 获取屏幕高度

        return f"{width}x{height}"  # 返回当前使用的屏幕分辨率（宽x高）

    # -----名人名言-----

    def 名人名言(self):  # 欸我去，def居然惊现中文字符😱！！！
        id = random.randint(1, 10)
        with open("./config/FamousQuotes.toml", 'rb') as f:
            famous_quotes = tomllib.load(f)
        text = famous_quotes[str(id)]
        return text
