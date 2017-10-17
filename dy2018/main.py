# -*- coding=utf8 -*-
import requests
import time

import sys
from bs4 import BeautifulSoup
import re
import re_utils
from model import model
from model.model import MovieInfo, Category
from proxy import proxy

base_url = 'http://www.dy2018.com'

headers = {
    "User-Agent": "Mozilla/5.1 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.2",
    # "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; CIBA) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


def fetch_movie_detail(movie_url):
    """
        保存电影详情
    :return: movieInfo
    """
    response = request(movie_url)
    # print(response.status_code)

    response.encoding = 'GBK'
    text = response.text
    # print(text)
    # print('sys.getdefaultencoding()', sys.getdefaultencoding())
    try:
        text = str(text, encoding='utf-8')
    except:
        pass
    # print('utf-8', text)
    soup = BeautifulSoup(text, 'lxml')
    movie_info = MovieInfo()
    movie_info.url = movie_url
    # title_all 2017年印度7.1分动作片《巴霍巴利王(下)：终结》BD中英双字
    movie_info.title = soup.find("h1").text
    movie_info.title_all = soup.find("h1").text
    # print(movie.title_all)
    div_zoom = soup.find(id='Zoom')
    div_zoom_text = str(div_zoom.get_text)
    # print(type(div_zoom))
    # print(div_zoom.get_text)
    movie_info.poster_url = div_zoom.find('img')['src']
    # print(movie.poster_url)
    movie_info.other_name = group1(re.search(r'<p>◎译　　名　(.*?)</p>', div_zoom_text))
    print(movie_info.other_name)
    movie_info.source_name = group1(re.search(r'<p>◎片　　名　(.*?)</p>', div_zoom_text))# 原名
    # print(movie.source_name)
    movie_info.year = group1(re.search(r'<p>◎年　　代　(.*?)</p>', div_zoom_text))
    # print(movie.year)
    movie_info.area = group1(re.search(r'<p>◎产　　地　(.*?)</p>', div_zoom_text))
    # print(movie.area)
    movie_info.category_list = group1(re.search(r'<p>◎类　　别　(.*?)</p>', div_zoom_text))
    # print(movie.category_list)
    movie_info.language_list = group1(re.search(r'<p>◎语　　言　(.*?)</p>', div_zoom_text))
    # print(movie.language_list)
    movie_info.caption = group1(re.search(r'<p>◎字　　幕　(.*?)</p>', div_zoom_text))
    # print(movie.caption)
    movie_info.douban_rating = group1(re.search(r'<p>◎豆瓣评分　(.*?)</p>', div_zoom_text))
    # print(movie.douban_rating)
    movie_info.measure_size = group1(re.search(r'<p>◎视频尺寸　(.*?)</p>', div_zoom_text))
    # print(movie.measure_size)
    movie_info.file_size = group1(re.search(r'<p>◎文件大小　(.*?)</p>', div_zoom_text))
    # print(movie.file_size)
    movie_info.showing_time = group1(re.search(r'<p>◎片　　长　(.*?)</p>', div_zoom_text))
    # print(movie.showing_time)
    movie_info.director = group1(re.search(r'<p>◎导　　演　(.*?)</p>', div_zoom_text))
    # print(movie.director)
    movie_info.actor_list = re_utils.re_get_actor(div_zoom_text)
    # print(movie.actor_list)
    movie_info.brief = re_utils.re_get_brief(div_zoom_text)
    # print(movie_info.brief)
    movie_info.behind_to_make = re_utils.re_get_behind(div_zoom_text)
    # print(movie_info.behind_to_make)
    movie_info.film_picture_url = re_utils.re_get_film_picture_url(div_zoom_text)
    # print("film_picture_url = ", movie_info.film_picture_url)
    movie_info.xunlei_url_list = re_utils.re_get_xunlei_url(div_zoom_text)
    # print("xunlei_url_list = ", movie_info.xunlei_url_list)
    # print(type(movie_info))
    return movie_info


def group1(match):
    if match:
        return match.group(1)
    return ''


def get_movie_detail_url(page_url):
    """
    得到当前页面上所有电影列表的url
    :return: []
    """
    # pages = ['http://www.dy2018.com/0/index.html',
    #          # 'http://www.dy2018.com/0/index_2.html',
    #          ]
    # for page_url in pages:
    re = request(page_url)
    re.encoding = 'GBK'
    soup = BeautifulSoup(re.text, 'lxml')
    tag_ul = soup.find(class_="co_content8").ul
    # print("tag_ul = ",tag_ul.get_text)
    cur_page_movie_urls = []
    for child in tag_ul.find_all("table"):
        tag_a = child.find_all(title=True)[0]  # 含有title属性的标签
        cur_page_movie_urls.append(base_url + tag_a['href'])
    # print(base_url + tag_a['href'], "  ", str(tag_a['title']).strip())
    # pass
    return cur_page_movie_urls


def get_movie_page(cate):
    try:
        re = request(cate.url)
    except:
        change_proxy = True
    # print(cate.name)
    re.encoding = 'GBK'  # 设置编码
    # print(re.encoding)
    soup = BeautifulSoup(re.text, 'lxml')
    # print(soup.get_text)
    tag_select = soup.find_all(name="select")[0]  # 查找标签tag
    # print(soup.title)
    # print(tag_select.text)
    cate.pages = ['http://www.dy2018.com' + child['value'] for child in tag_select.children]
    # print(cate.pages)
    # for index,child in enumerate(tag_select.children):
    #     # print(child.name)
    #     cate.pages[index] = 'http://www.dy2018.com'+child['value']
    #     # print(cate.pages[index])


proxies_hostname = []
change_proxy = False


def init_proxies():
    global proxies_hostname
    if len(proxies_hostname) == 0:  # 初始化代理
        with open('../test/proxy_ips.txt', 'r') as file:
            proxies_hostname = file.readlines()
    print("init_proxies", len(proxies_hostname))


def request(url):
    global proxies_hostname
    global change_proxy
    if change_proxy:  # 需要更换代理
        proxies_hostname.remove(proxies_hostname[0])
        change_proxy = False
    try:
        proxy_name = proxies_hostname[0]
    except:
        print("没有代理了")
        raise BaseException("没有代理了")

    proxies = {
        'http': str(proxy_name).replace('\n', ''),
    }
    print("代理:{}, url:{}".format(proxies, url))
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
    except:
        change_proxy = True
        # error url:http://www.dy2018.com/0/index_2.html
        # error : HTTPConnectionPool(host='180.97.235.30', port=80): Max retries exceeded with url: http://www.dy2018.com/0/index_2.html (Caused by ProxyError('Cannot connect to proxy.', NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000024CA5C3FA20>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。',)))

        return request(url)
    if resp.status_code != 200:
        return request(url)
    return resp


def start_spider():
    model.init_model()  # 初始化数据库

    cate = Category("http://www.dy2018.com/0/", '剧情片')  # 手动初始化一个分类

    get_movie_page(cate)  # 获取当前分类的所有页1~n
    i = 0
    for url in cate.pages:
        time.sleep(2)
        try:
            movie_urls = get_movie_detail_url(url)
        except BaseException as e:
            print('error url:' + url + ' \nerror : ' + str(e))
            change_proxy = True
            continue
        for movie_url in movie_urls:
            # print(type(movie))
            try:
                movie_exist = MovieInfo.get(MovieInfo.url == movie_url)  # 过滤重复的电影
                if movie_exist:
                    continue
            except:
                pass

            time.sleep(1)
            try:
                movie = fetch_movie_detail(movie_url)
                # print('result', movie.source_name)
                movie.save()
                print("保存的电影{index}：{name}".format(index=i, name=movie.source_name))
                i += 1
            except BaseException as e:
                print('error url:' + movie_url + ' \nerror : ' + str(e))
                pass


if __name__ == "__main__":
    init_proxies()
    start_spider()
