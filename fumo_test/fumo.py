import base64
import hashlib
import random
import re

import requests
import subprocess

from bs4 import BeautifulSoup

from fumo_test import config
from rediss import myredis

header = {
    'Cache-Control': 'private',
    'Connection': 'close',
    'User-Agent': 'HTTP SyncML Client [en] (WinNT; I)',
    'Accept-Language': 'en',
    'Accept-Charset': 'utf-8',
    # 'Host': "127.0.0.1\:9081",
    'Content-Type': 'application/vnd.syncml.dm+xml',
    # 'Content-Type': 'application/vnd.syncml.dm+wbxml',
}


def start_pkg(pkg, num):
    if 'xml' == config.protocol:
        header['Content-Type'] = 'application/vnd.syncml.dm+xml'
    elif 'wbxml' == config.protocol:
        header['Content-Type'] = 'application/vnd.syncml.dm+wbxml'

    print('---- start:', pkg, num, header['Content-Type'])
    # 第一个pkg1发送
    if 'wbxml' in header['Content-Type']:
        transfer('{}/{}{}.xml'.format(config.root_path, pkg, num))

        with open('{}/{}{}.wbxml'.format(config.root_path, pkg, num), 'rb') as file:
            buf = file.read()
    else:
        with open('{}/{}{}.xml'.format(config.root_path, pkg, num), 'rb') as file:
            buf = file.read()

    header['Content-Length'] = str(len(buf))
    print('content length=', header['Content-Length'])

    str_buf = str(buf, encoding='utf-8')

    # 替换device_id
    if num == 11:
        config.session = str(random.random())

    str_buf = str_buf.replace('{{session_id}}', config.session)
    str_buf = str_buf.replace('{{device_id}}', config.client_username)

    if num == 3:
        # 生成客户端nonce
        # 生成cred密钥
        str_buf = str_buf.replace('{{cred_b64}}',
                                  calc_b64(config.client_username,
                                           config.client_password,
                                           config.server_nonce))
        str_buf = str_buf.replace('{{nonce}}', str(base64.b64encode(config.nonce_client_1),
                                                   encoding='utf-8'))
    if num == 5:
        str_buf = str_buf.replace('{{nonce}}', str(base64.b64encode(config.nonce_client_2),
                                                   encoding='utf-8'))

    if num == 11:
        str_buf = str_buf.replace('{{cred_b64}}',
                                  calc_b64(config.client_username,
                                           config.client_password,
                                           myredis.get('redis_client_nonce')))
        str_buf = str_buf.replace('{{Correlator}}',
                                  str(myredis.get("redis:correlator"),encoding='utf-8'))

    request_data = str_buf
    print('request url:', config.fumo_url)
    print('request data:', request_data)
    resp = requests.post(url=config.fumo_url, data=request_data, headers=header)

    print(resp.status_code)
    print('response data:', resp.text)  # wbxml

    # pkg2接收
    if 'wbxml' in header['Content-Type']:
        with open('{}/{}{}.wbxml'.format(config.root_path, pkg, num + 1), 'wb') as file:
            file.write(resp.content)

        transfer('{}/{}{}.wbxml'.format(config.root_path, pkg, num + 1))

        with open('{}/{}{}.xml'.format(config.root_path, pkg, num + 1), 'r') as file:
            resp_xml = file.read()


    else:
        with open('{}/{}{}.xml'.format(config.root_path, pkg, num + 1), 'wb') as file:
            file.write(resp.content)
            resp_xml = resp.text

    # 返回的是pkg2
    if num == 1:
        # <NextNonce xmlns='syncml:metinf'>Oz9cODA3MiUmRmsoSkZxIw==</NextNonce>
        # server_nonce=\
        nonce_b64 = re.search('<NextNonce(.*)>(.*)</NextNonce>',
                              resp_xml).group(2)
        print('server nonce_b64:', nonce_b64)
        config.server_nonce = base64.b64decode(nonce_b64)
        print('server nonce:', config.server_nonce)
    # 返回的是pkg4:校验服务器
    if num == 3:
        soup = BeautifulSoup(resp_xml.replace('\\n', ''), 'xml')
        b64_secret = soup.find('Cred').Data.text
        calc_secret = calc_b64(config.server_username, config.server_password,
                               config.nonce_client_1)
        if not b64_secret == calc_secret:
            raise BaseException("认证服务器不通过")

        nonce_b64 = re.search('<NextNonce(.*)>(.*)</NextNonce>',
                              resp_xml).group(2)
        config.server_nonce = base64.b64decode(nonce_b64)
        # 存放客户端nonce
        myredis.set('redis_client_nonce', config.server_nonce)
        print('保存客户端nonce进redis')

    # 保存correlator
    if num == 7:
        correlator = re.search('<Correlator>(.*)</Correlator>',
                              resp_xml).group(1)
        print("Correlator=",correlator)
        myredis.set('redis:correlator', correlator)

    print('---- end:', pkg, num + 1)


def calc_b64(username, password, nonce):
    """
    :return: B64(MD5(B64(MD5(username:password)):nonce)
    """
    print('calc_b64:', username, password, nonce)
    m1 = hashlib.md5()
    m1.update('{}:{}'.format(username, password).encode("utf8"))
    md5_u_p = m1.digest()  # MD5(username:password)
    print('MD5(username:password)', md5_u_p)
    b64_1 = base64.b64encode(md5_u_p)  # B64(MD5(username:password))
    print('B64(MD5(username:password))', b64_1)
    m2 = hashlib.md5()
    m2.update(b64_1)
    m2.update(b':')
    m2.update(nonce)
    md5_u_p = m2.digest()  # MD5(B64(MD5(username:password)):nonce)
    b64_2 = base64.b64encode(md5_u_p)
    print('cred', b64_2)
    return str(b64_2, encoding='utf-8')


def transfer(file_path):
    exec_cmd("java -jar wbxml.jar {}".format(file_path))


def exec_cmd(cmd_str):
    print(cmd_str)
    p = subprocess.Popen(cmd_str, shell=True)
    p.wait()
