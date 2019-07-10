import requests

resp = requests.post(url='https://iotapi.adups.com/product/1506449997/24cd4d496fb67d2VSmx/ota/checkVersion',
              json='{"mid":"P1QRMYGXMK","version":"20180118-0923","networkType":"WIFI"}')

print(resp.status_code)
print(resp.text)