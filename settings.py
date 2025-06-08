import tomllib
import os
from loguru import logger
import tomli_w
from maliang import theme

import settingsGUI

# 全局配置变量
_config = None
_config_path = './config/config.toml'
_update_path = './config/update_config.toml'


def _ensure_config_dir():
    """确保配置目录存在"""
    os.makedirs(os.path.dirname(_config_path) or '.', exist_ok=True)


def load_config():
    """
    加载配置文件
    如果文件不存在，创建默认配置
    返回: 配置字典
    """
    global _config

    try:
        logger.info(f"尝试加载配置文件: {_config_path}")
        with open(_config_path, 'rb') as f:
            _config = tomllib.load(f)
        logger.info("配置文件加载成功")
        return _config
    except FileNotFoundError:
        logger.info("配置文件不存在，创建默认配置")
        _ensure_config_dir()

        default_config = {
            "Cache": True,
            "ExperienceTheFeatures": False,
            "UseRegistry": True,
            "appearance": {"color_mode": 0},
            "storage": {"cache": True},
            "update": {
                "url": "https://raw.githubusercontent.com/EECT/EECT_update/refs/heads/main/update.toml",
                "download_source": "0",
                "update_channel": "0"
            },
            "senior": {
                "ExperienceTheFeatures": False,
                "UseRegistry": True
            },
            "experimental": {
                "TitleBarFamousQuotes": False,
                "NoBetaWarner": True
            }
        }

        with open(_config_path, 'wb') as f:
            tomli_w.dump(default_config, f)

        _config = default_config
        return _config
    except Exception as e:
        logger.error(f"加载配置文件失败: {e}")
        raise


def get_config():
    """
    获取当前配置
    如果尚未加载，则先加载配置
    返回: 配置字典
    """
    global _config

    if _config is None:
        return load_config()

    return _config


def save_config():
    """
    保存当前配置到文件
    """
    global _config

    if _config is None:
        raise ValueError("配置未加载，无法保存")

    try:
        logger.info(f"保存配置到: {_config_path}")
        with open(_config_path, 'wb') as f:
            tomli_w.dump(_config, f)
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
    config = get_config()

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


def modify_config(key_path=None, new_value=None, **kwargs):
    """
    修改配置
    可以通过 key_path 和 new_value 直接修改，或者通过 kwargs 修改多个值
    """
    if key_path is not None and new_value is not None:
        set_value(key_path, new_value)
    elif kwargs:
        for k, v in kwargs.items():
            set_value(k, v)
    else:
        raise ValueError("必须提供 key_path 和 new_value 或者 kwargs")

    # 保存修改
    save_config()


def get_cache():
    """获取缓存设置"""
    return get_value("Cache")


def set_cache(value):
    """设置缓存设置"""
    set_value("Cache", value)
    # 自动保存
    save_config()


def get_experience_features():
    """获取体验功能设置"""
    return get_value("ExperienceTheFeatures")


def set_experience_features(value):
    """设置体验功能设置"""
    set_value("ExperienceTheFeatures", value)
    # 自动保存
    save_config()


def get_use_registry():
    """获取注册表功能设置"""
    return get_value("UseRegistry")


def get_color_mode():
    """
    获取颜色模式
    返回: 0-系统, 1-深色, 2-浅色
    """
    color_modes = {"0": "system", "1": "dark", "2": "light"}
    mode = get_value("appearance.color_mode")
    if str(mode) not in color_modes:
        raise ValueError("无效的颜色模式")
    mode = color_modes[str(mode)]
    return mode


def get_experimental_TitleBarFamousQuotes():
    """获取实验性功能设置"""
    return get_value("experimental.TitleBarFamousQuotes")


def set_use_registry(value):
    """设置注册表功能设置"""
    set_value("UseRegistry", value)
    # 自动保存
    save_config()


def set_color_mode(mode):
    """
    设置颜色模式
    :param mode: 0-系统, 1-深色, 2-浅色
    """
    color_modes = {"0": "system", "1": "dark", "2": "light"}
    theme.set_color_mode(color_modes[str(mode)])
    logger.info(f"切换主题至{color_modes[str(mode)]}")

    if str(mode) not in color_modes:
        raise ValueError("无效的颜色模式")

    # 确保 appearance 部分存在
    config = get_config()
    if "appearance" not in config:
        config["appearance"] = {}

    config["appearance"]["color_mode"] = mode
    _config = config  # 更新全局配置

    # 保存配置
    save_config()


def set_download_source(mode):
    """
    设置颜下载源
    :param mode: 0-github, 1-bgithub
    """
    source = {"0": "github", "1": "bgithub"}
    theme.set_color_mode(source[str(mode)])
    logger.info(f"切换下载源至{source[str(mode)]}")

    if str(mode) not in source:
        raise ValueError("无效的下载源")

    set_value("download_source", f"{mode}")

    # 保存配置
    save_config()


# 初始化加载配置
load_config()


if __name__ == "__main__":
    settingsGUI.main_window()