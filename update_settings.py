import tomllib
from loguru import logger
import os

import update_settingsGUI

config = None


def main():
    update_settingsGUI.main_window()


def get_config():
    logger.info("声明全局变量 config")
    global config

    try:
        logger.info("尝试读取配置文件 ./config/update_config.toml")
        with open('./config/update_config.toml', 'rb') as f:
            config = tomllib.load(f)
            download_source = config['download_source']
            update_channel = config['update_channel']

            logger.info("读取配置文件成功，返回 download_source, update_channel")
            return download_source, update_channel

    except FileNotFoundError:
        logger.info("配置文件不存在，创建默认配置文件")
        # 创建默认配置文件
        default_config = """
url = "https://raw.githubusercontent.com/EECT/EECT_update/refs/heads/main/update.toml"
download_source = "0"    # 0: github, 1: proxy
update_channel = "0"    # 0: 正式版, 1: 测试版
"""
        os.makedirs('./config', exist_ok=True)

        with open('./config/update_config.toml', 'w', encoding="utf-8") as f:
            f.write(default_config)
        config = tomllib.loads(default_config)
        logger.info("创建默认配置文件成功")


if __name__ == '__main__':
    main()
