import random

from bs4 import BeautifulSoup

from fumo_test import config
from fumo_test.fumo import start_pkg
from rediss import myredis


def no_error():
    print('>>>>>>>>>>>>>>start[no_error]>>>>>>>>>>>>>>')

    config.session = random_str()
    # config.root_path = 'client_pkgs_simple_check'
    config.root_path = 'client_pkgs'

    start_pkg('pkg', 1)
    start_pkg('pkg', 3)
    start_pkg('pkg', 5)
    start_pkg('pkg', 7)
    # start_pkg('pkg', 9)
    # start_pkg('pkg', 11)
    # start_pkg('pkg', 13)
    print('>>>>>>>>>>>>>>>>end[no_error]>>>>>>>>>>>>>>')

    pass

def update_nonce():
    print('>>>>>>>>>>>>>>start[update_nonce]>>>>>>>>>>>>>>')

    config.session = random_str()
    config.root_path = 'client_pkgs'

    start_pkg('pkg', 1)
    start_pkg('pkg', 3)

    print('new client nonce = ', myredis.get('client_nonce'))


def random_str():
    return str(random.random())


def start():
    # config.protocol = 'wbxml'
    # for i in range(0, 100):
    config.nonce_client_1 = (str(random.randint(1, 99999)) + "rewr").encode('utf-8')
    config.nonce_client_2 = (str(random.randint(1, 99999)) + "rewr").encode('utf-8')

    # print('-----------------------------------------------------------{}'.format(i))
    no_error()
    # error_1()


if __name__ == '__main__':
    start()
    # update_nonce()
    pass
