import random
import time

from datetime import date

from terminal_ import cmd_shell_


def pre_page():
    """
    向上翻页
    :return:
    """
    print("pre_page:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    cmd_shell_.exec_cmd("adb shell input keyevent 24")


def next_page():
    """
    向下翻页
    :return:
    """
    print("next_page:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    cmd_shell_.exec_cmd("adb shell input keyevent 25")


if __name__ == '__main__':

    for i in range(0, 300):
        time.sleep(random.randint(0, 10) / 10 * 4)
        if random.randint(0, 10) == 5:
            pre_page()
        else:
            next_page()

        time.sleep(random.randint(0, 10) / 10 * 4)
