# coding=utf-8

import requests
import sys
from bs4 import BeautifulSoup
import codecs

url = "https://developer.android.google.cn/samples/index.html"


def start():
    fetch_paged()


def fetch_paged():
    resp = requests.get(url)
    resp.encoding = "UTF-8"
    # <h2 class="blog-post-title"><a href="http://www.devtf.cn/?p=1264" rel="bookmark">高效地配置OkHttp</a></h2>
    # print(resp.text)
    parse_paged(resp.text)


def parse_paged(text):
    soup = BeautifulSoup(text, "lxml")
    div_tag = soup.find(class_="cols sample-grid")
    # print(div_tag.text)

    for a_tag in div_tag.find_all('a'):
        # print(type(a_tag))

        span_tag = a_tag.find(class_='sample-title')
        # print(span_tag.text)
        desc_tag = a_tag.find(class_='text')
        # print(desc_tag.text)

        with open("samples2.md", "a") as file:
            file.write(span_tag.text + '\n' + desc_tag.text + '\n')  # 写入的文件是GBK编码，不知道如何改为UTF8编码？
            # print(resp.text)
    print('end ...')



if __name__ == "__main__":
    start()

    # with codecs.open("main.html", "r", 'utf-8') as file:
    #     all_text = file.read()
    #     parse_paged(all_text)
