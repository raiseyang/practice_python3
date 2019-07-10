# -*- coding: utf-8 -*-

"""
input: the url of git book
output: the zip file of the git book
"""
import requests
from bs4 import BeautifulSoup


def start(url):
    if not url:
        raise ValueError('url is none')
    resp = requests.get(url=url)
    resp.encoding = "utf8"
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "lxml")
    # 找到<nav>节点
    nav = soup.find('nav')
    a_nav_list = nav.find_all('a')
    for a in a_nav_list:
        name = a['href']
        # 过滤非html
        if not name.endswith('.html'):
            continue
        link = url + name
        resp = requests.get(link)
        resp.encoding = 'utf8'

        save_file(name.replace('/', '__'), resp.text)
        print('loop', name)

    print(resp.encoding, 'end.')
