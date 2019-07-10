import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0,
                            password='adups2017'
                            )
r = redis.Redis(connection_pool=pool)


def set(key, value):
    """
    存放key value到redis
    :param key:
    :param value:
    :return:
    """
    r.set(key, value)


def get(key):
    return r[key]


def test():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0,
                                password='adups2017'
                                )
    r = redis.Redis(connection_pool=pool)

    r.set('python', '3')

    print(r.get('python'))
