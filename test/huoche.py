import requests

host = 'https://kyfw.12306.cn'
uri = '/otn/leftTicket/queryZ?' \
      'leftTicketDTO.train_date=2018-02-01' \
      '&leftTicketDTO.from_station=GIW' \
      '&leftTicketDTO.to_station=QRW' \
      '&purpose_codes=ADULT'

header = {
    'Host': 'kyfw.12306.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}


def start():
    # resp = requests.get(url=host + uri, headers=header)
    dict_a = {
        "aa": "aa",
        "aaa": ['a', 'b'],
        "bb": {
            "aa": 'aa',
        }
    }
    print(dict_a['bb']['aa'])
    # print(resp.text)

    pass


if __name__ == '__main__':
    start()
