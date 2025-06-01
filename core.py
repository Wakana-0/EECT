from loguru import logger
import tomllib
import traceback
import platform

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
    # 系统类型、版本和架构
    os_type = platform.system()
    os_version = platform.version()
    machine_arch = platform.machine()

    return os_type, os_version, machine_arch    # 返回 系统类型、版本、架构
