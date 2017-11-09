import json

import requests

url = "http://iotdown.mayitek.com/111147962/2222347/5a18be4d-da18-4971-a739-d9c99dbefe95.zip"

headers = {
    'cache-control': "no-cache",
    'Range': "bytes=212485881-",
    'postman-token': "0e7d23a0-066d-90e5-20b8-d1cfcd667e47"
}

response = requests.request("GET", url, headers=headers)
print(response.headers['Content-Length'])

print('end')

print(response.text)
