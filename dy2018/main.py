import requests
from bs4 import BeautifulSoup
import re
import re_utils

base_url = 'http://www.dy2018.com'


class MovieInfo(object):
    def __init__(self):
        self.title = None
        self.title_all = None
        self.poster_url = None
        self.other_name = None
        self.source_name = None
        self.year = None
        self.area = None
        self.category_list = []
        self.language_list = []
        self.caption = None
        self.douban_rating = None
        self.imdb_rating = None
        self.measure_size = None
        self.file_size = None
        self.showing_time = None
        self.director = None
        self.actor_list = []
        self.brief = None
        self.behind_to_make = None
        self.film_picture_url = None
        self.xunlei_url_list = []  # http://www.dy2018.com/i/98093.html


class Category(object):
    def __init__(self, url, name):
        self.name = name  # 类名：剧情
        self.url = url
        self.pages = []  # 该分类下每页的url

    def __str__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)

    def __repr__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)


def get_movie_detail():
    movie_detail_url = base_url + "/i/98256.html"
    response = requests.get(movie_detail_url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Cookie": """BAIDU_SSP_lcr=https://www.baidu.com/link?url=UJ2FI3a9GP4nHNplxkFJAw_5dcyWFBM05H5eaiEJdku&wd=&eqid=f0d0d05a0001c47900000004599b7a52; Hm_lvt_a68dc87e09b2a989eec1a0669bfd59eb=1503361427,1503364467,1503449614,1503563374; Hm_lpvt_a68dc87e09b2a989eec1a0669bfd59eb=1503578557"""
    })
    print(response.status_code)
    text = response.text
    de_text = text.encode("ISO-8859-1").decode("GBK")
    soup = BeautifulSoup(de_text, 'lxml')
    movie = MovieInfo()
    # title_all 2017年印度7.1分动作片《巴霍巴利王(下)：终结》BD中英双字
    movie.title_all = soup.find("h1").text
    print(movie.title_all)
    div_zoom = soup.find(id='Zoom')
    div_zoom_text = div_zoom.get_text
    # print(type(div_zoom))
    # print(div_zoom.get_text)
    movie.poster_url = div_zoom.find('img')['src']
    print(movie.poster_url)
    movie.other_name = re.search(r'<p>◎译　　名　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.other_name)
    movie.source_name = re.search(r'<p>◎片　　名　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.source_name)
    movie.year = re.search(r'<p>◎年　　代　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.year)
    movie.area = re.search(r'<p>◎产　　地　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.area)
    movie.category_list = re.search(r'<p>◎类　　别　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.category_list)
    movie.language_list = re.search(r'<p>◎语　　言　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.language_list)
    movie.caption = re.search(r'<p>◎字　　幕　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.caption)
    movie.douban_rating = re.search(r'<p>◎豆瓣评分　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.douban_rating)
    movie.measure_size = re.search(r'<p>◎视频尺寸　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.measure_size)
    movie.file_size = re.search(r'<p>◎文件大小　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.file_size)
    movie.showing_time = re.search(r'<p>◎片　　长　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.showing_time)
    movie.director = re.search(r'<p>◎导　　演　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.director)
    movie.actor_list = re_utils.re_get_actor(str(div_zoom.get_text))
    print(movie.actor_list)
    movie.brief = re.search(r'<p>◎简　　介　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.brief)
    movie.behind_to_make = re.search(r'<p>◎幕后制作　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.behind_to_make)
    movie.film_picture_url = re.search(r'<p>◎影片截图　(.*?)</p>', str(div_zoom.get_text)).group(1)
    print(movie.film_picture_url)


def get_movie_detail_url():
    """
    得到电影的名称及url
    :return:
    """
    pages = ['http://www.dy2018.com/0/index.html',
             # 'http://www.dy2018.com/0/index_2.html',
             ]
    for page_url in pages:
        re = requests.get(page_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            "Cookie": """BAIDU_SSP_lcr=https://www.baidu.com/link?url=UJ2FI3a9GP4nHNplxkFJAw_5dcyWFBM05H5eaiEJdku&wd=&eqid=f0d0d05a0001c47900000004599b7a52; Hm_lvt_a68dc87e09b2a989eec1a0669bfd59eb=1503361427,1503364467,1503449614; Hm_lpvt_a68dc87e09b2a989eec1a0669bfd59eb=1503478107"""
        })
        text = re.text
        de_text = text.encode("ISO-8859-1").decode("GBK")
        soup = BeautifulSoup(de_text, 'lxml')
        tag_ul = soup.find(class_="co_content8").ul
        # print("tag_ul = ",tag_ul.get_text)
        for child in tag_ul.find_all("table"):
            tag_a = child.find_all(title=True)[0]  # 含有title属性的标签
            print(base_url + tag_a['href'], "  ", str(tag_a['title']).strip())
        pass


def get_movie_page(cate):
    re = requests.get(cate.url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Cookie": """BAIDU_SSP_lcr=https://www.baidu.com/link?url=UJ2FI3a9GP4nHNplxkFJAw_5dcyWFBM05H5eaiEJdku&wd=&eqid=f0d0d05a0001c47900000004599b7a52; Hm_lvt_a68dc87e09b2a989eec1a0669bfd59eb=1503361427,1503364467,1503449614; Hm_lpvt_a68dc87e09b2a989eec1a0669bfd59eb=1503478107"""
    })
    # print(cate.name)
    text = re.text
    print(re.encoding)
    de_text = text.encode("ISO-8859-1").decode("GBK")  # 转换格式编码 encode()编码使用re.encoding decode解码使用document.characterSet
    soup = BeautifulSoup(de_text, 'lxml')
    print(soup.get_text)
    tag_select = soup.find_all(name="select")[0]  # 查找标签tag
    print(soup.title)
    # print(tag_select.text)
    cate.pages = ['http://www.dy2018.com' + child['value'] for child in tag_select.children]
    print(cate.pages)
    # for index,child in enumerate(tag_select.children):
    #     print(child.name)
    #     cate.pages[index] = 'http://www.dy2018.com'+child['value']
    #     print(cate.pages[index])


if __name__ == "__main__":
    cate = Category("http://www.dy2018.com/0/", '剧情片')
    # get_movie_page(cate)

    get_movie_detail()

    # response = requests.get("http://www.dy2018.com/0/")
    # print(response.encoding,response.status_code)
    #
    # # print(chardet.detect(response.encoding))
    # soup = BeautifulSoup(response.text.encode(str(response.encoding)), 'lxml')
    # print(soup.get_text)
    #
    # div_tag = soup.find_all("div", class_="co_content2")[0]
    #
    # category = []
    # for i, a in enumerate(div_tag.find_all("a")):  # 带有索引的for
    #     category.append(Category("http://www.dy2018.com" + a.get("href"), a.text))
    #     # print("http://www.dy2018.com" + a.get("href"), "  {} ".format(i), a.text)
    # print(list(category))
    # get_movie(category[0])
