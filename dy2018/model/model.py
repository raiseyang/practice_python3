"""
MovieInfo实体
"""
from peewee import MySQLDatabase, Model, CharField

db = MySQLDatabase('dy2018_db',
                   host="localhost",
                   user="root",
                   password="",
                   charset='utf8') # 注意这里一定不要向官网一样设置为：utf8mb4(四字节的utf8),必须和mysql一致


def init_model():
    db.connect()
    try:
        db.create_tables([MovieInfo])
    except:
        pass


class MovieInfo(Model):
    url = CharField(null=True)
    title = CharField(null=True)
    title_all = CharField(null=True)
    poster_url = CharField(null=True)
    other_name = CharField(null=True)
    source_name = CharField(null=True)
    year = CharField(null=True)
    area = CharField(null=True)
    category_list = CharField(null=True)
    language_list = CharField(null=True)
    caption = CharField(null=True)
    douban_rating = CharField(null=True)
    imdb_rating = CharField(null=True)
    measure_size = CharField(null=True)
    file_size = CharField(null=True)
    showing_time = CharField(null=True)
    director = CharField(null=True)
    actor_list = CharField(null=True,max_length=2000)
    brief = CharField(null=True,max_length=4000)
    behind_to_make = CharField(null=True,max_length=3000)
    film_picture_url = CharField(null=True)
    xunlei_url_list = CharField(null=True,max_length=1000)  # http://www.dy2018.com/i/98093.html

    class Meta:
        database = db  # This model uses the "people.db" database.


class Category(object):
    def __init__(self, url, name):
        self.name = name  # 类名：剧情
        self.url = url
        self.pages = []  # 该分类下每页的url

    def __str__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)

    def __repr__(self):
        return 'url = {0} ,name = {1}'.format(self.url, self.name)
