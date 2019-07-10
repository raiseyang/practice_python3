import requests

url = 'http://127.0.0.1:9081/upload'

files = {'logFile': open('req_body.log', 'rb')}

datas = {'vin': '2222',
         'deviceId': '3333',
         'correlator': '2332'}

resp = requests.post(url=url, files=files, data=datas)
print(resp.text)
