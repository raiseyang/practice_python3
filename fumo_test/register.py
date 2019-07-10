from fumo_test import config
from fumo_test.fumo import start_pkg
from fumo_test.main import random_str


def start():

    config.fumo_url = 'http://127.0.0.1:9081/fumo'
    config.session = random_str()
    config.root_path = 'regi'

    start_pkg('pkg', 1)
    start_pkg('pkg', 3)
    start_pkg('pkg', 5)

pass


if __name__ == '__main__':
    start()