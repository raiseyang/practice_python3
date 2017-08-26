from bs4 import BeautifulSoup

if __name__ == "__main__":

    soup = BeautifulSoup('<b><a class="ulink" href="/html/gndy/dyzz/">[最新电影]</a><a href="/html/gndy/dyzz/20070605/2666.html" class="ulink" title="变异食人怪物科幻大片《异形魔怪3》DVD中字">变异食人怪物科幻大片《异形魔怪3》DVD中字</a></b>',"lxml")
    print(soup.find_all(title=True)[0])
    print(type(soup.find_all(title=True)[0]['title']))
    text = '   2017年欧美7.9分喜剧片《希望的另一面》BD德语中字'
    print(text)
    print('',text.strip())

