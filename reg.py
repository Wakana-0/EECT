import winreg
from loguru import logger
import traceback
import err


# TODO:他奶奶的，快把任务栏星期做完！

def show_seconds_in_system_clock(value):    # 在任务栏上的时间显示秒
    logger.info("调用 show_seconds_in_system_clock 函数")
    try:
        logger.info("打开注册表项: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
        # 打开注册表项
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
            0,  # 保留参数
            winreg.KEY_SET_VALUE  # 写入权限
        )
        logger.info("修改注册表: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
        # 修改值（类型为REG_DWORD）
        winreg.SetValueEx(key, "ShowSecondsInSystemClock", 0, winreg.REG_DWORD, value)
        print(f"成功修改：ShowSecondsInSystemClock = {value}")
        logger.info(f"成功修改注册表 HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced 的值为{value}")
    except PermissionError as e:
        logger.error("没有权限修改注册表")
        err.show_error(traceback.format_exc(), 0)
        return e
    except FileNotFoundError:
        logger.error("注册表项 HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced 不存在，创建新的注册表项 HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
        # 创建键值（若不存在）
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
        winreg.SetValueEx(key, "ShowSecondsInSystemClock", 0, winreg.REG_DWORD, value)
        print(f"成功创建：ShowSecondsInSystemClock = {value}")
        winreg.CloseKey(key)
        show_seconds_in_system_clock(value)

    winreg.CloseKey(key)
    logger.info("关闭注册表")
    return True


def show_weekday_in_taskbar(value):  # 在任务栏上显示星期
    logger.info("调用 show_weekday_in_taskbar 函数")
    if value == 1:
        date = "yyyy/MM/dd ddd"
    else:
        date = "yyyy/M/d"

    try:
        logger.info("打开注册表项: HKEY_CURRENT_USER\Control Panel\International")
        # 打开注册表项
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Control Panel\International",
            0,
            winreg.KEY_SET_VALUE
        )
        # 修改短日期格式（添加 dddd 显示星期）
        logger.info(f"修改注册表 HKEY_CURRENT_USER\Control Panel\International 的值为{date}")
        winreg.SetValueEx(key, "sShortDate", 0, winreg.REG_SZ, date)
        logger.info(f"成功修改注册表 HKEY_CURRENT_USER\Control Panel\International 的值为{date}")
        print(f"已成功修改：任务栏日期将显示{date}")
        winreg.CloseKey(key)
        logger.info("关闭注册表")
    except PermissionError as e:
        logger.error("没有权限修改注册表")
        err.show_error(traceback.format_exc(), 0)
        return e
    except Exception as e:
        logger.error("修改注册表时出错，堆栈信息：\n" + traceback.format_exc())
        return e
    return True


if __name__ == "__main__":
    show_seconds_in_system_clock(1)  # （不）显示秒
    show_weekday_in_taskbar(0)  # （不）显示星期
