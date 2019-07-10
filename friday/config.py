host = "http://vehicle-manager.abupdate.com"

device_id = '740565fae72b87afe539d097484f897b'
secret = '9431bb9357671da631a2f025e336b5bd'

uri_register = "/v1/register"
uri_check = "/v1/%s/check" % device_id

# {"status":1000,"msg":"设备注册成功",
# "data":{"deviceId":"551d3e75e369fa1441383f49c3f78274",
# "devicePwd":"LWIA6h",
# "secret":"296c384b8720a8d1e9d1f43b8ac8c93a"}}


req_data_down_report = {"sessionId": "1518005108707",
                        "action": "down",
                        "timestamp": "1518005112057",
                        "sign": "2f535b9b94a53dccaf25ebee1a9afe70",
                        "report": [
                            {"ecuSId": "skpine8317",
                             "ecuSVer": "0.0.9",
                             "down_start": 1518005111939,
                             "down_end": 1518005111999,
                             "down_time": 1, "result": "3", "reason": ""}
                            , {"ecuSId": "LSM", "ecuSVer": "26249255", "down_start": -1,
                               "down_end": 1518005111773, "down_time": 3, "result": "3",
                               "reason": ""},
                            {"ecuSId": "TGC", "ecuSVer": "26690263", "down_start": -1,
                             "down_end": 1518005111898, "down_time": 3, "result": "3",
                             "reason": ""}]}

req_data_check = {
    "cmdId": "3",
    "token": "jac",
    "timestamp": "",
    "sign": "x",
    "sysConfig": {
        "storageSpace": "10000",
        "netType": "wifi",
        "lac": "x",
        "cid": "xx"
    },
    "ecus": [
        {
            "ecuSId": "HUT",
            "ecuDId": "HUT",
            "ecuSVer": "0.0.8",
            "ecuHVer": "1",
            "ecuHsn": "HUT",
            "upgradeType": 2
        },
        {
            "ecuSId": "DCU",
            "ecuDId": "DCU",
            "ecuSVer": "26249248",
            "ecuHVer": "1",
            "ecuHsn": "DCU",
            "upgradeType": 2
        },
        {
            "ecuSId": "NWC",
            "ecuDId": "NWC",
            "ecuSver": "26690247",
            "ecuHver": "1",
            "ecuHsn": "NWC",
            "upgradeType": 2
        }
    ]
}
 # {"status":1000,"msg":"设备注册成功","data":{"deviceId":"740565fae72b87afe539d097484f897b","devicePwd":"RhouUm","secret":"9431bb9357671da631a2f025e336b5bd"}}
req_data_register = {
    "vin": "Generic00{}",
    "model": "Generic ac8317",
    "subModel": "MTK8312",
    "sdkVersion": "python_1.0",
    "token": "jac",
    "timestamp": "",
    "sign": "x",
    "ecus": [
        {
            "ecuSId": "HUT",
            "ecuDId": "HUT",
            "ecuSVer": "0.0.8",
            "ecuHVer": "1",
            "ecuHsn": "HUT",
        },
        {
            "ecuSId": "DCU",
            "ecuDId": "DCU",
            "ecuSVer": "26249248",
            "ecuHVer": "1",
            "ecuHsn": "DCU",
        },
        {
            "ecuSId": "NWC",
            "ecuDId": "NWC",
            "ecuSver": "26690247",
            "ecuHver": "1",
            "ecuHsn": "NWC",
        }
    ]
}
