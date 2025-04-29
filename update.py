import requests
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
        version_code = data['version_code']
        date = data['date']
        changelog = data['changelog']
        importance = data['importance']
        return new_version, version_code, date, changelog, importance
    else:
        print(response.status_code)
        with open('./config/update.toml', 'rb') as f:
            update_data = tomllib.load(f)
            new_version = update_data['version']
            version_code = update_data['version_code']
            date = update_data['date']
            changelog = update_data['changelog']
            importance = update_data['importance']
            return new_version, version_code, date, changelog, importance

# 检查当前程序版本
def check_version(value):
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
    # 检查更新
    new_version, version_code, date, changelog, importance = check_update()
    if new_version is None:
        return False  # 如果没有更新，则返回False

    # 显示更新信息
    print(f"新版本: {new_version}")
    print(f"版本号: {version_code}")
    print(f"发布日期: {date}")
    print(f"更新日志: {changelog}")
    print(f"重要性: {importance}")
    compare_ver = compare_versions(check_version(1), new_version)
    print("对比版本号", compare_ver)
    return compare_ver, new_version, version_code, date, changelog, importance


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
