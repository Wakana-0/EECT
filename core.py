from loguru import logger
import tomllib
import traceback
import platform
import wmi

logger.info("加载EECT核心必要模块")
import GUI
import err


def version():
    return 1


def mian():
    read_config()
    GUI.main_window()


# -----配置文件区-----

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
    memory_size = int(os_mem.TotalVisibleMemorySize) / 1024 / 1024  # 总内存大小

    return memory_size    # 返回 总内存大小（GB）
