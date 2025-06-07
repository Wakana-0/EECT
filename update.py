import os
import tomllib
import traceback
import zipfile
import requests
from loguru import logger
from packaging import version


# 获取更新配置
def get_update_config():
    logger.info("调用函数 get_update_config")
    logger.info("获取当前更新配置")
    with open('./config/update_config.toml', 'rb') as f:
        update_config = tomllib.load(f)
        url = update_config['url']
        beta_url = update_config['beta_url']
        update_channel = update_config['update_channel']
        downloader_source = update_config['downloader_source']
    return url, beta_url, update_channel, downloader_source


# 检查更新
def check_update():
    logger.info("调用函数 check_update")
    # 检查是否有更新
    logger.info("开始检查更新")
    # 从指定更新通道检查更新
    if get_update_config()[2] == "0":
        logger.info("使用正式版更新通道")
        url = get_update_config()[0]  # 获取最新正式版
        response = requests.get(url, verify=False)  # verify=False用于忽略SSL证书验证
        try:
            logger.info("解析数据")
            data = response.text
            logger.info(f"获得的原始数据：\n{data}")
            data = tomllib.loads(data)

            new_version = data['version']
            version_code = data['version_code']
            date = data['date']
            changelog = data['changelog']
            importance = data['importance']
            zip_name = data['file_name']
            url = data['download_url']
            return new_version, version_code, date, changelog, importance, zip_name, url
        except Exception:
            logger.error(
                f"解析数据时出错。HTTP状态码：{response.status_code}\n\n堆栈信息：\n{traceback.format_exc()}\n\n获得的原始数据：\n{response.text}")
            print(
                f"解析数据时出错。HTTP状态码：{response.status_code}\n\n堆栈信息：\n{traceback.format_exc()}\n\n获得的原始数据：\n{response.text}")
            logger.info("使用本地数据")
            with open('./config/update.toml', 'rb') as f:
                update_data = tomllib.load(f)
                new_version = update_data['version']
                version_code = update_data['version_code']
                date = update_data['date']
                changelog = update_data['changelog']
                importance = update_data['importance']
                zip_name = update_data['file_name']
                url = update_data['download_url']
                return new_version, version_code, date, changelog, importance, zip_name, url

    else:
        logger.info("使用Beta版更新通道")
        url = get_update_config()[1]  # 获取最新Beta
        response = requests.get(url, verify=False)  # verify=False用于忽略SSL证书验证
        try:
            logger.info("解析数据")
            data = response.text
            logger.info(f"获得的原始数据：\n{data}")
            data = tomllib.loads(data)

            new_version = data['version']
            version_code = data['version_code']
            date = data['date']
            changelog = data['changelog']
            importance = data['importance']
            zip_name = data['file_name']
            url = data['download_url']
            return new_version, version_code, date, changelog, importance, zip_name, url
        except Exception:
            logger.error(
                f"解析数据时出错。HTTP状态码：{response.status_code}\n\n堆栈信息：\n{traceback.format_exc()}\n\n获得的原始数据：\n{response.text}")
            print(
                f"解析数据时出错。HTTP状态码：{response.status_code}\n\n堆栈信息：\n{traceback.format_exc()}\n\n获得的原始数据：\n{response.text}")
            logger.info("使用本地数据")
            with open('./config/update.toml', 'rb') as f:
                update_data = tomllib.load(f)
                new_version = update_data['version']
                version_code = update_data['version_code']
                date = update_data['date']
                changelog = update_data['changelog']
                importance = update_data['importance']
                zip_name = update_data['file_name']
                url = update_data['download_url']
                return new_version, version_code, date, changelog, importance, zip_name, url


def check_version(value):  # 检查当前程序版本
    logger.info("调用函数 check_version")
    logger.info("获取当前程序版本")
    # 检查版本
    with open('./config/version.toml', 'rb') as f:
        version_data = tomllib.load(f)
        current_version = version_data['version']
        version_code = version_data['version_code']
        if value == 1:
            return current_version
        else:
            return version_code


# 比较版本号
def compare_versions(current_version, update_version):
    current_version = version.parse(current_version)
    update_version = version.parse(update_version)
    if current_version >= update_version:
        return False
    else:
        return True


def update():
    logger.info("调用函数 update")
    # 检查更新
    new_version, version_code, date, changelog, importance, zip_name, url = check_update()
    if new_version is None:
        return False  # 如果没有更新，则返回False

    # 显示更新信息
    print(f"新版本: {new_version}")
    print(f"版本号: {version_code}")
    print(f"发布日期: {date}")
    print(f"更新日志: {changelog}")
    print(f"重要性: {importance}")
    print(f"下载链接: {url}")
    print(f"文件名: {zip_name}")
    compare_ver = compare_versions(check_version(1), new_version)
    print("对比版本号", compare_ver)
    logger.info("版本信息：\n最新版本：%s\n版本号：%s\n发布日期：%s\n更新日志：%s\n重要性：%s\n下载链接：%s\n文件名：%s" % (
    new_version, version_code, date, changelog, importance, url, zip_name))
    return compare_ver, new_version, version_code, date, changelog, importance, zip_name, url


def unzip_file(zip_path, extract_to):
    logger.info("调用函数 unzip_file")
    logger.info(f"准备解压文件，从{zip_path}解压到{extract_to}")
    print(f"准备解压文件，从{zip_path}解压到{extract_to}")
    """
    解压 .zip 文件到指定目录

    :param zip_path: 要解压的 .zip 文件路径
    :param extract_to: 解压目标目录
    """
    try:
        # 检查 zip 文件是否存在
        if not os.path.exists(zip_path):
            logger.error(f"解压文件不存在: {zip_path}")
            print(f"找不到需要解压的文件：{zip_path}")
            return False

        # 检查目标目录是否存在，不存在则创建
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        # 解压文件
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            logger.info(f"成功解压 {zip_path} 到 {extract_to}")
            print("解压完成")
            return True

    except zipfile.BadZipFile:
        logger.error(f"文件不是有效的 .zip 文件: {zip_path}")
        print("解压失败，文件不是有效的 .zip 文件")
    except Exception as e:
        logger.error(f"解压失败: {e}")
        print(f"解压失败: {e}")
    return False


if __name__ == '__main__':
    ud = update()
    print(ud[0])
    if ud[0]:
        print(f"有新版本可用！详细信息：{ud[1]} {ud[2]} {ud[3]} {ud[4]}")
    else:
        print("没有新版本可用！")

"""
cw保佑



                                                ..:---:.              
                                     .::-=+**#%%@@@@@@@@#:            
                         .::-=++*##%%@@@@@@@@@@@@@@@@@@@@@:           
             ..:-==+*##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++=-       
    :==+**#%%@@@@@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#.     
  +%@@@@@@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%####%=     
:%@@@@@@@@@@%%%%%%%%########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%+:-:. 
%@@@@@@@%###################%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@#++++-
@@@@@@@@#######%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%%%%#=++++
@@@@@@@@@%%%%@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@@@%%@@@@@%%%%%%%%%%%%%%%%%%#%@@@#+++=+@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@%%@@@%#****%#++===%%%%-::.. +@%@-    =@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@%@@#=:..    +*     *%%* .... :%%%.....#@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@%-    .:::.+%- .. =%#: ..... +%*... -@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@%: ..:+**##**#+ .. -%+ . :: . :%= ...*@@@@@@@@@@@@%%%%%#+++++
@@@@@@@%@= ...*%########: ...#: . += .. *- . -%%@@@@@@@@@@@%%%%%#+++++
@@@@@@@%%:...:%%%%%%%%##= ...=.. :#*:.. :: . *@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@%%- ...=%%%%%##%##....... +##= ......:%%@@@@@@@@@@@@%%%%%#+++++
@@@@@@@%%*. .. .:--:.*%##= .... :####: .... +@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@%%*-.        *%##*......+%%%%+...:::#%@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@%%%%*+=====+*#%%%#*++***#%%%%%#####%%@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#+++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@#++++-
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@%+===: 
=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#+.      
 :#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=:::.         
    :------------------------------------------------:.               


                                                                      """
