import maliang
from maliang import theme
import tomllib
import os
from loguru import logger

import settingsGUI

config = None


def get_config():
    logger.info("调用 get_config 函数")
    logger.info("声明全局变量 config")
    global config
    try:
        logger.info("尝试读取配置文件 ./config/config.toml")
        with open('./config/config.toml', 'rb') as f:
            config = tomllib.load(f)
            ExperienceTheFeatures = config['ExperienceTheFeatures']
            Cache = config['Cache']
            UseRegistry = config['UseRegistry']
            logger.info("读取配置文件成功，返回 ache, ExperienceTheFeatures, UseRegistry")
            return Cache, ExperienceTheFeatures, UseRegistry
    except FileNotFoundError:
        logger.info("配置文件不存在，创建默认配置文件")
        # 创建默认配置文件
        default_config = """
# 使用缓存
Cache = true
# 体验功能
ExperienceTheFeatures = false
# 使用与注册表相关的功能
UseRegistry = true
"""
        os.makedirs('./config', exist_ok=True)
        with open('./config/config.toml', 'w', encoding="utf-8") as f:
            f.write(default_config)
        config = tomllib.loads(default_config)
        logger.info("创建默认配置文件成功")



def save_config(cache_val, exp_val, reg_val):
    logger.info("调用 save_config 函数")
    """保存新的配置到文件"""
    new_config = f"""
# 使用缓存
Cache = {str(cache_val).lower()}
# 体验功能
ExperienceTheFeatures = {str(exp_val).lower()}
# 使用与注册表相关的功能
UseRegistry = {str(reg_val).lower()}
"""
    logger.info("尝试保存配置到文件 ./config/config.toml")
    with open('./config/config.toml', 'w', encoding="utf-8") as f:
        f.write(new_config)
    logger.info("保存配置成功")

'''
def settingsGUI(window):
    logger.info("调用 settingsGUI 函数")
    logger.info("创建窗口 settings_window")
    settings_window = maliang.Toplevel(window, size=(500, 350), icon="./img/EECT_logo.ico")
    settings_window.center()
    settings_window_cv = maliang.Canvas(settings_window, auto_zoom=False)
    settings_window_cv.place(width=600, height=350)
    settings_window.title("设置")
    settings_window.resizable(False, False)

    # 获取初始配置
    logger.info("获取初始配置")
    cache_val, exp_val, reg_val = get_config()

    # GUI界面
    logger.info("创建设置界面")
    settings_text = maliang.Text(settings_window_cv, (20, 20), text="设置 - 所有设置均在重启软件后生效")

    # 创建开关控件并保存引用
    cache_switch = maliang.Switch(settings_window_cv, (10, 60))
    cache_switch.set(cache_val)
    maliang.Text(settings_window_cv, (80, 60), text="使用缓存")

    exp_switch = maliang.Switch(settings_window_cv, (10, 110))
    exp_switch.set(exp_val)
    maliang.Text(settings_window_cv, (80, 110), text="体验功能")

    reg_switch = maliang.Switch(settings_window_cv, (10, 160))
    reg_switch.set(reg_val)
    maliang.Text(settings_window_cv, (80, 160), text="使用注册表相关功能")
    
    # 添加保存按钮
    def on_save():
        logger.info("调用 on_save 函数")
        new_cache = cache_switch.get()
        new_exp = exp_switch.get()
        new_reg = reg_switch.get()
        save_config(new_cache, new_exp, new_reg)

        save_tip = maliang.Toplevel(settings_window, size=(300, 70), title="已保存你所做出的更改")
        theme.customize_window(save_tip, hide_button="maxmin")
        save_tip.toolwindow(True)
        save_tip.topmost(True)
        save_tip.center()
        save_tip_cv = maliang.Canvas(save_tip, auto_zoom=False)
        save_tip_cv.place(width=300, height=70)

        save_tip_text = maliang.Text(save_tip_cv, (40, 10), text="所有更改都已经保存，\n但重启软件后更改才会生效。", fontsize=16)


    save_btn = maliang.Button(settings_window_cv, (200, 250), text="保存更改", command=on_save)
'''

if __name__ == "__main__":
    settingsGUI.main_window()