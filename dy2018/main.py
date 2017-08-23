import requests
from bs4 import BeautifulSoup


class Category(object):
    def __init__(self, url, name):
        self.name = name
        self.url = url
        self.pages = []

    def __str__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)

    def __repr__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)


def get_movie():
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
            print(child.name)
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

    get_movie()

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
