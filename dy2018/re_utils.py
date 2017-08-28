import re

from bs4 import BeautifulSoup


def re_get_actor(html):
    """
    获取主演
    :param html:
    :return:
    """
    a = re.search(r'<p>◎主　　演　(.*)</p>\n(<p>　　　　　　(.*)</p>\n)*', html).group(0)
    line_list = a.split("\n")
    actors = [re.match(r'<p>(◎主\u3000\u3000演)?[\u3000]+(.*)</p>', tag_p).group(2) for tag_p in line_list if
              re.match(r'<p>(◎主\u3000\u3000演)?[\u3000]+(.*)</p>', tag_p)]
    return actors


def re_get_brief(html):
    """
    获取简介
    :param html:
    :return:
    """
    match = re.search(r'<p>◎简　　介(.*)</p>\n(<p>　　(.*)</p>\n)*', html).group(0)
    line_list = match.split("\n")
    # print(line_list)
    brief = ''
    for tap_p in line_list:
        # print(tap_p)
        match = re.match(r'<p>(.*?)</p>', tap_p)
        s = ''
        if match:
            s = match.group(1)
        # print(s)
        if s and not s.startswith('◎'):
            brief = brief + s + '\n'
    return brief


def re_get_behind(html):
    """
    获取幕后制作
    :param html:
    :return:
    """
    try:
        match = re.search(r'<p>◎幕后制作(.*)</p>\n(<p>　　(.*)</p>\n)*', html).group(0)
    except BaseException:
        return ''
    line_list = match.split("\n")
    # print(line_list)
    brief = ''
    for tap_p in line_list:
        # print(tap_p)
        match = re.match(r'<p>(.*?)</p>', tap_p)
        s = ''
        if match:
            s = match.group(1)
        print(s)
        if s and not s.startswith('◎'):
            brief = brief + s + '\n'
    return brief


def re_get_film_picture_url(html):
    try:
        search = re.search(r'<p>◎影片截图</p>\n<(div|p)>(?P<image>.*?)</(div|p)>', html).group('image')
    except BaseException:
        return ''
    return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')


def re_get_xunlei_url(html):
    # return re.findall('thunder://\w+?=?', html)
    soup = BeautifulSoup(html, 'lxml')
    xl_urls = []
    for tag_a in soup.find_all('a'):
        xl_urls.append(tag_a.text)
    return xl_urls
