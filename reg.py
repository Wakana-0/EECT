import winreg


def show_seconds_in_system_clock(value):    # 在任务栏上的时间显示秒
    try:
        # 打开注册表项
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
            0,  # 保留参数
            winreg.KEY_SET_VALUE  # 写入权限
        )
        # 修改值（类型为REG_DWORD）
        winreg.SetValueEx(key, "ShowSecondsInSystemClock", 0, winreg.REG_DWORD, value)
        print(f"成功修改：ShowSecondsInSystemClock = {value}")
    except PermissionError as e:
        return e
    except FileNotFoundError:
        # 创建键值（若不存在）
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
        winreg.SetValueEx(key, "ShowSecondsInSystemClock", 0, winreg.REG_DWORD, value)
        winreg.CloseKey(key)
        show_seconds_in_system_clock(value)

    winreg.CloseKey(key)
    return True


def show_weekday_in_taskbar(value):  # 在任务栏上显示星期
    if value == 1:
        date = "yyyy/MM/dd ddd"
    else:
        date = "yyyy/M/d"

    try:
        # 打开注册表项
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Control Panel\International",
            0,
            winreg.KEY_SET_VALUE
        )
        # 修改短日期格式（添加 dddd 显示星期）
        winreg.SetValueEx(key, "sShortDate", 0, winreg.REG_SZ, date)
        print(f"已成功修改：任务栏日期将显示{date}")
        winreg.CloseKey(key)
    except Exception as e:
        return e
    return True


if __name__ == "__main__":
    show_seconds_in_system_clock(1)  # （不）显示秒
    show_weekday_in_taskbar(0)  # （不）显示星期
