import requests
from bs4 import BeautifulSoup


class Category(object):
    def __init__(self, url, name):
        self.name = name
        self.url = url

    def __str__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)

    def __repr__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)


def get_movie(cate):
    re = requests.get(cate.url)
    print(cate.name)
    text = re.text
    soup = BeautifulSoup(text.encode(str(re.encoding)), 'lxml')
    select = soup.find_all(attrs={"onchange":"self.location.href=this.options[this.selectedIndex].value"})[0]
    print(soup.title)
    print(select.text)


if __name__ == "__main__":
    response = requests.get("http://www.dy2018.com/0/")
    print(response.encoding)

    # print(chardet.detect(response.encoding))
    soup = BeautifulSoup(response.text.encode(str(response.encoding)), 'lxml')
    # print(soup.get_text)

    div_tag = soup.find_all("div", class_="co_content2")[0]

    category = []
    for i, a in enumerate(div_tag.find_all("a")):  # 带有索引的for
        category.append(Category("http://www.dy2018.com" + a.get("href"), a.text))
        # print("http://www.dy2018.com" + a.get("href"), "  {} ".format(i), a.text)
    print(list(category))
    get_movie(category[0])
