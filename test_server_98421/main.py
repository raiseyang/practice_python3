import os
import string
import re

from flask import Flask, request, redirect, url_for, send_file, Response

app = Flask(__name__)

field_json = {
    "pkg_num": 1,
    "dd_file_path": ".\\dd_file\\dd.txt",
    "update_file_path": ".\\update_file\\mock_package.zip",
    "test_fumo": False
    # "test_fumo": True
}


def re_get_session_id(xml):
    # <SessionID>2DF</SessionID>
    # return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')
    return re.search(r'<SessionID>(?P<id>.*?)</SessionID>', xml).group('id')


def re_get_msg_id(xml):
    # <MsgID>1</MsgID>
    # return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')
    return re.search(r'<MsgID>(?P<msg_id>.*?)</MsgID>', xml).group('msg_id')


def re_get_client_uri(xml):
    # <SessionID>2DF</SessionID>
    # return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')
    search = re.search(r'<Source><LocURI>(?P<LocURI>.*?)</LocURI><LocName>(?P<LocName>.*?)</LocName></Source>', xml)
    loc_uri = search.group('LocURI')
    loc_name = search.group('LocName')
    return (loc_uri, loc_name)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # http://127.0.0.1:5000/hello
    return ".hello"


response = [
    ("token", "123456"),
    ('Content-Type', 'application/vnd.syncml.dm+xml')
]
dd_response_header = [
    ("token", "123456"),
    ('Content-Type', 'application/vnd.oma.dd+xml')
]


@app.route('/dongsheng/dm', methods=['GET', 'POST'])
def dongsheng_dm():
    # http://127.0.0.1:5000/hello
    # 获取post请求的数据
    data = request.get_data()
    session_id = re_get_session_id(str(data))
    (loc_uri, loc_name) = re_get_client_uri(str(data))
    msg_id = re_get_msg_id(str(data))
    print("msg_id={},req={}".format(str(msg_id), str(data).encode("utf-8")))

    # 下载升级上报
    if "org.openmobilealliance.dm.firmwareupdate.downloadandupdate" in str(data):
        return open('server_pkgs/du_pkg2.txt').read().replace('${session_id}', session_id) \
                   .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                   .replace('${msg_id}', msg_id) \
            , "200", response
    # 检测版本
    if "org.openmobilealliance.dm.firmwareupdate.userrequest" in str(data):
        if msg_id == "1":
            # if field_json["pkg_num"] == 1:
            #     field_json["pkg_num"] = 3
            return open('server_pkgs/pkg2.txt').read().replace('${session_id}', session_id) \
                       .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                       .replace('${msg_id}', msg_id) \
                , "200", response
    if msg_id == "2":
        # if field_json["pkg_num"] == 3:
        #     field_json["pkg_num"] = 5
        if field_json['test_fumo'] :
            return open('server_pkgs/pkg4.txt').read().replace('${session_id}', session_id) \
                   .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                   .replace('${msg_id}', msg_id) \
            , "200", response
        else :
            return open('server_pkgs/pkg4_info.txt').read().replace('${session_id}', session_id) \
                       .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                       .replace('${msg_id}', msg_id) \
                , "200", response
    if msg_id == "3":
        # if field_json["pkg_num"] == 5:
        #     field_json["pkg_num"] = 7
        if field_json['test_fumo'] :
            return open('server_pkgs/pkg6.txt').read().replace('${session_id}', session_id) \
                   .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                   .replace('${msg_id}', msg_id) \
            , "200", response
        else:
            return open('server_pkgs/pkg6_info.txt').read().replace('${session_id}', session_id) \
                       .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                       .replace('${msg_id}', msg_id) \
                , "200", response
    if msg_id == "4":
        # if field_json["pkg_num"] == 7:
        #     field_json["pkg_num"] = 99
        return open('server_pkgs/pkg8.txt').read().replace('${session_id}', session_id) \
                   .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
                   .replace('${msg_id}', msg_id) \
            , "200", response
    # if field_json["pkg_num"] == 99:
    #     return open('server_pkgs/pkg99.txt').read().replace('${session_id}', session_id) \
    #                .replace('${loc_uri}', loc_uri).replace('${loc_name}', loc_name) \
    #                .replace('${msg_id}', msg_id) \
    #         , "200", response
    return "error:call dongsheng"


# @app.route('/reset', methods=['GET'])
# def reset():
#     # pkg_num=0
#     field_json["pkg_num"] = 1
#     return "the next pkg_num={}".format(field_json["pkg_num"])


# DeprecationWarning: The 'attachment_filename' parameter has been renamed to 'download_name'. The old name will be removed in Flask 2.1.
@app.route('/download_dd_file', methods=['GET', 'POST'])
def download_dd_file():
    # http://192.168.50.134:5000/download_dd_file

    size = os.path.getsize(field_json['update_file_path'])
    return open(field_json['dd_file_path']).read().replace('${package_size}', "{}".format(size)) \
        , 200, dd_response_header
    # return send_file(
    #     field_json['dd_file_path'],
    #     download_name="dd.txt", as_attachment=True), 200, dd_response_header


@app.route('/download_package', methods=['GET', 'POST'])
def download_package():
    # http://192.168.50.134:5000/download_package
    return send_file(
        field_json['update_file_path'],
        download_name="dd.txt", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
