import requests
from bs4 import BeautifulSoup

# url = 'http://localhost:4000/yi_chang_ff08_exceptions.html'
import  os

url = 'https://leohxj.gitbooks.io/a-programmer-prepares/content/index.html'
book_name = '程序员的自我修养'

# url = 'https://marcorosso.gitbooks.io/oma-device-management/'


def start():
    resp = requests.get(url=url)
    resp.encoding = "utf8"
    # resp.encoding = "ANSI"
    print(resp.text)
    soup = BeautifulSoup(resp.text, "lxml")
    nav = soup.find('nav')
    a_nav_list = nav.find_all('a')
    for a in a_nav_list:
        name = a['href']

        if not name.endswith('.html'):
            continue
        link = url + name
        resp = requests.get(link)
        resp.encoding = 'utf8'

        save_file(name.replace('/','__'), resp.text)
        print('loop', name)

    print(resp.encoding, 'end.')


def save_file(name, content):
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    with open('{}/{}'.format(book_name,name), 'w', encoding='utf8') as file:
        file.write(content)


if __name__ == '__main__':
    start()
