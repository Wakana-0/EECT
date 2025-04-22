import maliang
import webbrowser


def thanks(window):
    thanks_window = maliang.Toplevel(window, size=(400, 250))
    thanks_window.center()
    thanks_window_cv = maliang.Canvas(thanks_window, auto_zoom=False)
    thanks_window_cv.place(width=400, height=250)
    thanks_window.title("鸣谢")

    thanks_text = maliang.Text(thanks_window_cv, (20, 20), text="此程序使用了以下开源项目：")
    thanks_maliang = maliang.IconButton(thanks_window_cv, (20, 60), text="Maliang", image=maliang.PhotoImage(file="./img/maliang_logo.png").resize(32, 32), command=lambda: webbrowser.open_new_tab("https://github.com/Xiaokang2022/maliang"))


def list_of_developers(window):
    developers_window = maliang.Toplevel(window, size=(400, 250))
    developers_window.center()
    developers_window_cv = maliang.Canvas(developers_window, auto_zoom=False)
    developers_window_cv.place(width=400, height=250)
    developers_window.title("开发人员名单")

    developers_text = maliang.Text(developers_window_cv, (20, 20), text="开发者：\n\nLyang1273 - 代码、图标\nWakana-0 - 协助")


def open_source_license(window):
    license_window = maliang.Toplevel(window, size=(584, 430))
    license_window.center()
    license_window_cv = maliang.Canvas(license_window, auto_zoom=False)
    license_window_cv.place(width=584, height=445)
    license_window.title("开放源代码许可")

    license_text = maliang.Text(license_window_cv, (20, 5), text="本软件遵照 MIT License 开源协议开放源代码")
    license = maliang.Label(license_window_cv, (5, 50), text="""MIT License

Copyright (c) 2025 EECT Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""", fontsize=12)


if __name__ == "__main__":
    root = maliang.Tk()
    thanks(root)
    list_of_developers(root)
    open_source_license(root)
    root.mainloop()
