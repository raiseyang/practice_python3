import requests

server_url = "http://localhost:8088/"


def register():
    file = open('req_body', 'rb')
    content = file.read()

    requests.post(url=server_url + 'funambol/register', data=content)

    print('end')

if __name__ == '__main__':
    register()
