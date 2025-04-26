# TODO:整理代码

import requests
import urllib3
import tomllib
from packaging import version


# 获取更新配置
def get_update_config():
    with open('./config/update_config.toml', 'rb') as f:
        update_config = tomllib.load(f)
        url = update_config['url']
    return url


# 检查更新
def check_update():
    # 检查是否有更新
    url = get_update_config()
    response = requests.get(url, verify=False)  # verify=False用于忽略SSL证书验证
    if response.status_code == 200:
        data = response.text
        data = tomllib.loads(data)

        new_version = data['version']
        date = data['date']
        changelog = data['changelog']
        importance = data['importance']

        return new_version, date, changelog, importance


'''
def download_update():  # 下载更新
    response = requests.get(check_update()[3], verify=False)  # verify=False用于忽略SSL证书验证
    if response.status_code == 200:
        with open('update.zip', 'wb') as file:
            file.write(response.content)
        return True, response.status_code
    else:
        return False, response.status_code
'''


# 检查当前程序版本
def check_version():
    # 检查版本
    with open('./config/version.toml', 'r', encoding="utf-8") as f:
        data = f.read()
    version = tomllib.loads(data)
    current_version = version['version']    # 当前程序版本

    return version


# 比较版本号
def compare_versions():
    # 使用packaging库来比较版本号
    v1 = version.parse(check_version()['version'])
    v2 = version.parse(check_update()[0])
    if v1 == v2:
        return False
    elif v1 < v2:
        return True
    else:
        return False


def main():
    return compare_versions()


if __name__ == '__main__':
    print(check_update())
    print(compare_versions())
    print(main())
    # download_update()
