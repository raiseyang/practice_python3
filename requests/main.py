import requests

url = "http://fota4.adups.cn/ota/open/checkVersion"

headers = {
    'cache-control': "no-cache",
    'postman-token': "0e7d23a0-066d-90e5-20b8-d1cfcd667e47"
}

payload = {
    "mid": "12345postman",
    "version": "DW028_MT2502C_V1.0_HITN_170607_20170607-1625",
    "oem": "szkct",
    "models": "DW028_HITN_B",
    "token": "d07cde9de1af60b8dc799912f7f73f67",
    "platform": "MTK2502",
    "deviceType": "health",
    "sdkVerCode": "1",
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
