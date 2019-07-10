from time import time

import requests
import hmac
import hashlib

from friday import config


def get_time_stamp():
    return str(int(time()))


def hmac_(key, text):
    enc_res = hmac.new(key, text, hashlib.md5).hexdigest()
    return str(enc_res)


def check():
    req_data = config.req_data_check
    req_data["timestamp"] = get_time_stamp()
    #    "vin": "VIN01",
    # "model": "ac8317",
    # "subModel": "MTK8312",
    req_data["sign"] = hmac_(bytes(config.secret, encoding='utf-8'),
                             bytes(config.device_id +
                                   req_data["timestamp"], encoding='utf-8'))

    print(dict(req_data))
    resp = requests.post(config.host + config.uri_check, json=req_data)
    print(resp.text)


def register():
    vin_list = list(range(5, 20))


    for num in vin_list:
        req_data = config.req_data_register

        str_num = ""

        if len(str(num)) == 1:
            str_num = "0"+str(num)
        print(str_num)
        req_data["vin"] = "Generic0{}".format(str(str_num))
        req_data["timestamp"] = get_time_stamp()
        #    "num": "VIN01",
        # "model": "ac8317",
        # "subModel": "MTK8312",
        req_data["sign"] = hmac_(bytes(req_data["token"], encoding='utf-8'),
                                 bytes(req_data["vin"] +
                                       req_data["model"] +
                                       req_data["subModel"] +
                                       req_data["timestamp"], encoding='utf-8'))

        print(dict(req_data))
        resp = requests.post(config.host + config.uri_register, json=req_data)
        print(resp.text)


def update_report():
    json = {"deviceId": "c842a1ad88d0103eeb901c781140483b", "sessionId": "1518079092671",
            "action": "upgrade", "timestamp": "1518079218",
            "sign": "878094c812198d2936e9d11d22e872db", "report": [
            {"ecuSId": "skpine8317", "ecuSVer": "0.0.9", "upgrade_start": 1518079125,
             "upgrade_end": 1518079218, "result": "2", "reson": ""},
            {"ecuSId": "LSM", "ecuSVer": "26249255", "upgrade_start": 1518079116,
             "upgrade_end": 1518079120, "result": "2", "reson": ""},
            {"ecuSId": "TGC", "ecuSVer": "26690263", "upgrade_start": 1518079120,
             "upgrade_end": 1518079124, "result": "2", "reson": ""}]}
    resp = requests.post(
        "http://vehicle-manager.abupdate.com/v1/c842a1ad88d0103eeb901c781140483b/upgrade/report",
        json=json)
    print(resp.text)


if __name__ == '__main__':
    register()
    # check()
    # print(get_time_stamp())
    # update_report()

#  device_id = c842a1ad88d0103eeb901c781140483b,secret = 8bb97b174d0de8607fc6ab64951393e6.
#     result = hmac_(bytes('8bb97b174d0de8607fc6ab64951393e6',encoding='utf-8'),
#           bytes('Generic001'+'1518079092671'+'1518079218',encoding='utf-8'))
#     print(result)

pass
