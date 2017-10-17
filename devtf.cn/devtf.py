# coding=utf-8

import requests
import sys
from bs4 import BeautifulSoup
import codecs

url = "http://www.devtf.cn"


def start():
    for paged in range(1, 23):
        fetch_paged(paged)


def fetch_paged(cur_page):
    params = {
        "cat": 2,
        "paged": cur_page,
    }

    resp = requests.get(url, params=params)
    resp.encoding = "UTF-8"
    # <h2 class="blog-post-title"><a href="http://www.devtf.cn/?p=1264" rel="bookmark">高效地配置OkHttp</a></h2>
    # print(resp.text)
    parse_paged(resp.text)


def parse_paged(text):
    soup = BeautifulSoup(text, "lxml")
    h2_tags = soup.find_all("h2")  # 查找h2标签

    for tag in h2_tags:
        # print(tag.text)  # 文章标题
        # print(tag.find("a")["href"])  # 文章连接
        article = "[{}]({})\n".format(tag.text, tag.find("a")["href"])
        article = str(article)
        with open("article.md", "a") as file:
            file.write(article)  # 写入的文件是GBK编码，不知道如何改为UTF8编码？
            # print(resp.text)


if __name__ == "__main__":
    start()

    # with codecs.open("main.html", "r", 'utf-8') as file:
    #     all_text = file.read()
    #     parse_paged(all_text)
