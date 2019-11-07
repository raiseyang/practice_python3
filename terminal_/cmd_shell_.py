# -*- coding:utf-8 -*-
import subprocess
import platform

is_windows = platform.system() == 'Windows'


def exec_cmd(cmd_str):
    """
    cmd_str = "{} d {}.apk".format(apktool_path, file_name).split(' ')
    :param cmd_str:
    :return:
    """
    print(list(cmd_str))
    p = subprocess.Popen(cmd_str, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=is_windows)
    p.wait()
    return p.stdout.readlines()
