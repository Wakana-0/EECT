import maliang
from maliang import theme
import oobeGUI
from tkinter import messagebox


def cheek_file():
    try:
        with open('./config/setup.txt', 'rb') as f:
            return True
    except FileNotFoundError:
        return False


def initialize_file():
    try:
        with open("./config/config.toml", "w", encoding="utf-8") as f:
            f.write("""# 使用缓存
Cache = true
# 体验功能
ExperienceTheFeatures = false
# 使用与注册表相关的功能
UseRegistry = true""")
        with open("./config/update_config.toml", "w", encoding="utf-8") as f:
            f.write('url = "https://raw.githubusercontent.com/EECT/EECT_update/refs/heads/main/update.toml"')
    except Exception as e:
        messagebox.showerror("EECT OOBE", f"初始化配置文件失败，详细信息：\n{e}")
        return False


def set_username(inputbox_name, cv):
    username = inputbox_name.get()

    if username is None or username == "":
        messagebox.showerror("EECT OOBE", "用户名不能为空！")
    else:
        try:
            with open("./config/UserConfig.toml", "w", encoding="utf-8") as f:
                f.write(f'username = "{inputbox_name.get()}"')
                oobeGUI.color(cv)
            return True
        except Exception as e:
            messagebox.showerror("EECT OOBE", f"设置用户名失败，详细信息：\n{e}")


def set_color(mode):
    if mode == 0:
        theme.set_color_mode("system")
    elif mode == 1:
        theme.set_color_mode("dark")
    else:
        theme.set_color_mode("light")


def oobe():
    OOBE = maliang.Tk(size=(800, 500), icon="./img/EECT_logo.ico")
    OOBE.center()
    OOBE.title("EECT OOBE")
    OOBE.resizable(False, False)
    OOBE_home_cv = maliang.Canvas(OOBE, auto_zoom=False)
    OOBE_home_cv.place(width=800, height=500)

    OOBE_title_text = maliang.Text(OOBE_home_cv, (20, 20), text="你好，欢迎使用EECT！", fontsize=32)
    OOBE_text = maliang.Text(OOBE_home_cv, (20, 80), text="在正式开始使用EECT前，你需要先调整一些小设置。", fontsize=20)
    OOBE_home_next_button = maliang.Button(OOBE_home_cv, (650, 450), text="    下 一 步  ▶ ", command=lambda: oobeGUI.article(OOBE_home_cv))

    OOBE.mainloop()


if __name__ == "__main__":
    if not cheek_file():
        oobe()
