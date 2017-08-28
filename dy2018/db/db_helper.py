import pymysql

cursor = None


def open():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="",
                         db="dy2018_db",
                         charset='utf8')
    print('打开数据库连接')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # print(type(cursor))
    print('获得游标cursor')
    return cursor


# 创建表
def create_table():
    table_name = 'category'
    try:
        cursor.execute("select * from %s limit 1" % table_name)
        if cursor.fetchall():
            print('删除所有数据')
            cursor.execute("delete from %s" % table_name)
            return
    except:
        print('创建表')
        sql = " \
            CREATE TABLE %s ( \
        `id` int(11) NOT NULL AUTO_INCREMENT, \
        `girl_id` varchar(255) COLLATE utf8_bin NOT NULL, \
        `girl_pic_url` varchar(255) COLLATE utf8_bin NOT NULL, \
        `girl_pic_length` varchar(255) COLLATE utf8_bin NOT NULL, \
        PRIMARY KEY (`id`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin \
        AUTO_INCREMENT=1 ; \
        " % table_name

        cursor.execute(sql)

        db.commit()


if __name__ == '__main__':
    open()
