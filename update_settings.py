import tomllib

import tomli_w
from loguru import logger
import os

import update_settingsGUI

config = None
_update_config_path = './config/update_config.toml'


def main():
    update_settingsGUI.main_window()


def _ensure_config_dir():
    """确保配置目录存在"""
    os.makedirs(os.path.dirname(_update_config_path) or '.', exist_ok=True)


def load_config():
    """
    加载配置文件
    如果文件不存在，创建默认配置
    返回: 配置字典
    """
    global config

    try:
        logger.info(f"尝试加载配置文件: {_update_config_path}")
        with open(_update_config_path, 'rb') as f:
            config = tomllib.load(f)
        logger.info("配置文件加载成功")
        return config
    except FileNotFoundError:
        logger.info("配置文件不存在，创建默认配置")
        _ensure_config_dir()

        default_config = {
            "url": "https://raw.bgithub.xyz/EECT/EECT_update/refs/heads/main/update.toml",
            "beta_url": "https://raw.bgithub.xyz/EECT/EECT_update/refs/heads/main/update-beta.toml",
            "download_source": "0",
            "update_channel": "0"
        }

        with open(_update_config_path, 'wb') as f:
            tomli_w.dump(default_config, f)

        config = default_config
        return config
    except Exception as e:
        logger.error(f"加载配置文件失败: {e}")
        raise


def get_config():
    """
    获取当前配置
    如果尚未加载，则先加载配置
    返回: 配置字典
    """
    global config

    if config is None:
        return load_config()

    return config


def save_config():
    """
    保存当前配置到文件
    """
    global config

    if config is None:
        raise ValueError("配置未加载，无法保存")

    try:
        logger.info(f"保存配置到: {_update_config_path}")
        with open(_update_config_path, 'wb') as f:
            tomli_w.dump(config, f)
        logger.info("配置保存成功")
        return True
    except Exception as e:
        logger.error(f"保存配置失败: {e}")
        return False


def get_value(key_path):
    """
    获取配置值
    :param key_path: 键路径，如 "ExperienceTheFeatures" 或 "appearance.color_mode"
    :return: 对应的值
    """
    config = load_config()

    keys = key_path.split('.')
    current = config

    try:
        for k in keys:
            current = current[k]
        return current
    except (KeyError, TypeError) as e:
        logger.error(f"获取配置值失败: {e}")
        raise KeyError(f"键路径 '{key_path}' 不存在")


def set_value(key_path, value):
    """
    设置配置值
    :param key_path: 键路径，如 "ExperienceTheFeatures" 或 "appearance.color_mode"
    :param value: 要设置的值
    """
    config = get_config()

    keys = key_path.split('.')
    current = config

    try:
        # 遍历到目标键的前一级
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        # 设置值
        if value == "True":
            value = "true"
        elif value == "False":
            value = "false"

        current[keys[-1]] = value
        logger.info(f"设置配置值: {key_path} = {value}")
        save_config()
    except (KeyError, TypeError) as e:
        logger.error(f"设置配置值失败: {e}")
        raise KeyError(f"键路径 '{key_path}' 无效")


def set_download_source(value):
    """
    设置下载源
    :param value: 0-github, 1-bgithub
    """
    source = {"0": "github", "1": "bgithub"}
    logger.info(f"切换下载源至{source[str(value)]}")

    if str(value) not in source:
        raise ValueError("无效的下载源")

    set_value("download_source", f"{value}")

    # 保存配置
    save_config()


def set_update_channel(value):
    """
    设置更新检查频道
    :param value: 0: 正式版, 1: 测试版
    """
    channel = {"0": "正式版", "1": "Beta版"}
    logger.info(f"切换更新频道至{channel[str(value)]}")

    if str(value) not in channel:
        raise ValueError("无效的更新频道")

    set_value("update_channel", f"{value}")

    # 保存配置
    save_config()


# 初始化加载配置
load_config()


if __name__ == '__main__':
    main()
