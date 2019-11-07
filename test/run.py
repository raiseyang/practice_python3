# -*- coding:utf-8 -*-
import os, sys
import shutil
from sys import argv
import threading
import subprocess
import platform

file_name = 'iot_fota'
apktool_path = ''
is_windows = platform.system() == 'Windows'
if is_windows:
    apktool_path = str(os.path.join(sys.path[0], 'apktool'))
else:
    apktool_path = "./apktool"


def start():
    if not len(argv) == 3:
        print('错误:请输入id,secret')
        return
    print(platform.platform(), 'python={}'.format(platform.python_version()))
    delete_temp_file()  # 清除上次产生的文件
    print('0%开始制作')
    decoding()  # 解码apk
    modify_data(argv[1], argv[2])  # 替换数据
    building()  # 打包apk
    copy_dist_apk()  # 拷贝新的apk
    delete_temp_file()  # 删除临时文件
    print('100%请签名后使用'.format(file_name))


def decoding():
    """
    解码apk
    :return:
    """
    cmd_de = "{} d {}.apk".format(apktool_path, file_name).split(' ')
    exec_cmd(cmd_de)
    print("40%解压完成")


def modify_data(id, secret):
    print('50%需要替换的数据为：id={},secret={}'.format(id, secret))
    with open('{}/AndroidManifest.xml'.format(file_name), 'r') as file:
        content = file.read()
        content = content.replace('string/00000000000', 'string/{}'.format(id))
        content = content.replace('string/11111111111111111111111111111111', 'string/{}'.format(secret))

    with open('{}/AndroidManifest.xml'.format(file_name), 'w') as file:
        file.write(content)
    pass


def building():
    cmd_b = "{} b {}".format(apktool_path, file_name).split(' ')
    exec_cmd(cmd_b)


def copy_dist_apk():
    src_file = '{name}/dist/{name}.apk'.format(name=file_name)
    dist_file = '{}_new.apk'.format(file_name)
    shutil.copy(src_file, dist_file)


def delete_temp_file():
    if os.path.exists(file_name):
        shutil.rmtree(file_name)


def exec_cmd(cmd_str):
    print(list(cmd_str))
    p = subprocess.Popen(cmd_str, shell=is_windows)
    p.wait()


if __name__ == '__main__':
    start()
