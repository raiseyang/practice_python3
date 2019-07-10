import os
import re

import requests
import subprocess
import platform
import sys

from fumo_test import config

header = {
    'Cache-Control': 'private',
    'Connection': 'close',
    'User-Agent': 'HTTP SyncML Client [en] (WinNT; I)',
    'Accept-Language': 'en',
    'Accept-Charset': 'utf-8',
    # 'Host': "127.0.0.1\:9081",
    'Content-Type': 'application/vnd.syncml.dm+xml',
    # 'Content-Type': 'application/vnd.syncml.dm+wbxml',
}

# base_url = 'http://omatest.adups.com:19093'
base_url = 'http://localhost:9082'

url1 = base_url + '/redis/addEcuTask?ecuName=ICM'
url2 = base_url + '/redis/addEcuTask?ecuName=ICI'
url3 = base_url + '/redis/addEcuTask?ecuName=FW'
url4 = base_url + '/redis/addCar'
url5 = base_url + '/redis/mget'
url6 = base_url + '/redis/test/addICIEcuTask'
url7 = base_url + '/redis/test/addICMEcuTask'
url8 = base_url + '/redis/test/addCar'


def start_test():
    # response = requests.get(url='https://leohxj.gitbooks.io/a-programmer-prepares/content/index.html')
    # print(response.text)

    # requests.get(url=url1)
    # requests.get(url=url2)
    # requests.get(url=url3)
    # requests.get(url=url4)
    # requests.get(url=url5)
    requests.get(url=url6)
    requests.get(url=url7)
    resp = requests.get(url=url8)
    print(resp.text)

    pass


if __name__ == "__main__":
    start_test()
