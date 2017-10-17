"""
https://www.oschina.net/translate/sqlalchemy-vs-orms
https://peewee.readthedocs.io/en/latest/peewee/quickstart.html
Thing	Corresponds to...
Model class	Database table
Field instance	Column on a table
Model instance	Row in a database table
"""
from datetime import datetime, date

import pymysql
from peewee import *

# db = SqliteDatabase('people.db')
# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
# db = pymysql.connect(host="localhost",
#                      user="root",
#                      password="",
#                      db="peewee_db_test1",
#                      charset='utf8mb4')
# print(type(db))
# MySQLDatabase为peewee内部对象
db = MySQLDatabase('peewee_db_test1',
                   host="localhost",
                   user="root",
                   password="",
                   charset='utf8mb4')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


# 增加
def insert_a_person():
    Person.create(name='bob', birthday=date(1960, 1, 15), is_relative=True)


# 删除
def delete_a_person():
    bob = find_a_person('bob')
    bob.delete_instance()


# 查找
def find_a_person(name):
    return Person.get(Person.name == 'bob')


# 修改
def refresh_a_person():
    bob = find_a_person('bob')
    bob.name = 'bob1'
    bob.save()


if __name__ == "__main__":
    db.connect()
    # db.create_tables([Person, Pet])
    insert_a_person()
    # print(type(find_a_person('bob')))
    # delete_a_person()
    # refresh_a_person()
    print('end.')
