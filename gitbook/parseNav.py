from bs4 import BeautifulSoup


class Article(object):
    title = ''
    chapter = ''
    href = ''

    def __str__(self):
        return 'title={},chapter={},href={}'.format(self.title, self.chapter, self.href)

    def __repr__(self):
        return 'title={},chapter={},href={}'.format(self.title, self.chapter, self.href)


def start(nav, book_name):
    string = ''

    with open(nav, 'rb') as file:
        string = file.read()

    soup = BeautifulSoup(string, 'lxml')

    lis = soup.find_all('li', attrs={"data-level": True})

    list_article = []
    for li in lis:
        article = Article()
        article.chapter = li['data-level']
        article.title = li.find('a').text
        article.href = li.find('a')['href']
        list_article.append(article)
    # print(list(list_article))

    with open('chapters', 'w', encoding='utf8')as file:
        file.write('--{}--\n'.format(book_name))
        for article in list_article:
            file.write(article.chapter + "%%%" + article.title + "%%%" + article.href)
            file.write('\n')


if __name__ == '__main__':
    start('nav.xml', 'Kotlin in action')
