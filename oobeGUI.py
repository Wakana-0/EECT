import maliang
import about
import EECT_oobe
import time


def article(cv):
    cv.clear()
    article_title = maliang.Text(cv, (20, 20), text="在这之前，你需要先仔细阅读EECT的使用条款。")
    open_source_license = maliang.Button(cv, (20, 80), text="开放源代码许可", command=lambda: about.open_source_license(cv))
    free_software_statement = maliang.Button(cv, (20, 140), text="EECT免费软件声明", command=lambda: about.free_software_statement(cv))
    next_button = maliang.Button(cv, (650, 450), text="    下 一 步  ▶ ", command=lambda: initialize(cv))
    last_button = maliang.Button(cv, (500, 450), text="     退 出     ", command=lambda: exit(0))


def initialize(cv):
    cv.clear()
    initialize_wait = maliang.Spinner(cv, (20, 20), mode="indeterminate")
    initialize_title = maliang.Text(cv, (70, 20), text="即将开始初始化配置文件，准备好后点击“继续”。")
    initialize_next_button = maliang.Button(cv, (650, 450), text="    继 续  ▶ ", command=lambda: initializing(initialize_title, initialize_next_button))
    last_button = maliang.Button(cv, (500, 450), text=" ◀  上 一 步    ", command=lambda: article(cv))

    def initializing(title, button):
        title.destroy()
        button.destroy()
        initialize_title = maliang.Text(cv, (70, 20), text="正在初始化配置文件，请稍等。")
        EECT_oobe.initialize_file()
        time.sleep(0.5)
        initialize_title.destroy()
        initialize_wait.destroy()
        initialize_title = maliang.Text(cv, (70, 20), text="初始化完成！点击“下一步”继续。")
        initialize_next_button = maliang.Button(cv, (650, 450), text="    下 一 步  ▶ ", command=lambda: username(cv))


def username(cv):
    cv.clear()
    username_title = maliang.Text(cv, (20, 20), text="输入你的用户名，用户名只会保存在本地，因此你可以使用自己的名字或者……外号？")
    username_input = maliang.InputBox(cv, (20, 80), placeholder="输入用户名")
    username_next_button = maliang.Button(cv, (650, 450), text="    下 一 步  ▶ ", command=lambda: EECT_oobe.set_username(username_input, cv))


def color(cv):
    cv.clear()
    color_title = maliang.Text(cv, (20, 20), text="选择颜色模式")
    color_mode = maliang.SegmentedButton(cv, (20, 80), text=("跟随系统", "深色", "浅色"), default=0)
    apply = maliang.Button(cv, (280, 85), text="    应 用    ", command=lambda: EECT_oobe.set_color(color_mode.get()))
    color_next_button = maliang.Button(cv, (650, 450), text="    下 一 步  ▶ ")


def update_settings(cv):
    cv.clear()
    update_title = maliang.Text(cv, (20, 20), text="更新设置")
    update_text = maliang.Text(cv, (20, 80), text="设置EECT的检查更新模式")

    update_next_button = maliang.Button(cv, (650, 450), text="    下 一 步  ▶ ")
