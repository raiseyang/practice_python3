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
    cmd_shell_.exec_cmd("adb -s 1019030 shell input keyevent 24")


def next_page():
    """
    向下翻页
    :return:
    """
    print("next_page:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    cmd_shell_.exec_cmd("adb -s 1019030  shell input keyevent 25")


def three_hundred_in_20_min():
    for i in range(0, 300):
        time.sleep(random.randint(0, 10) / 10 * 3)
        if random.randint(0, 10) == 5:
            pre_page()
        else:
            next_page()

        time.sleep(random.randint(0, 10) / 10 * 3)


def three_hundred_in_10_min():
    for i in range(0, 300):
        time.sleep(random.randint(0, 10) / 10)
        if random.randint(0, 10) == 5:
            pre_page()
        else:
            next_page()

        time.sleep(random.randint(0, 10) / 10)


def three_hundred_in_1_min():
    for i in range(0, 300):
        time.sleep(random.randint(0, 10) / 10)
        if random.randint(0, 10) == 5:
            pre_page()
        else:
            next_page()


if __name__ == '__main__':
    three_hundred_in_20_min()
    # three_hundred_in_10_min()
    # three_hundred_in_1_min()
