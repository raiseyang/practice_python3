import random
import subprocess

import os
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/funambol/dm', methods=['GET', 'POST'])
def hello_world():
    data = request.get_data()  # application/json

    cache_name = 'cache/{}.wbxml'.format(random.randint(0, 9999999999))

    with open(cache_name, 'wb')as file:
        file.write(data)

    transfer(cache_name)

    print('request data:', open(cache_name.replace('wbxml', 'xml')).read())

    result_file_path = 'pkg2.xml'
    transfer(result_file_path)
    return open(result_file_path.replace('xml', 'wbxml')).read()


# class SyncApp(Resource):
#
#     def post(self):
#         data = request.get_data()  # application/json
#
#         cache_name = 'cache/{}.wbxml'.format(random.randint(0,9999999999))
#
#         with open(cache_name,'wb')as file:
#             file.write(data)
#
#         transfer(cache_name)
#
#         print('request data:',open(cache_name.replace('wbxml','xml')).read())
#
#         result_file_path = 'pkg2.xml'
#         transfer(result_file_path)
#         return open(result_file_path.replace('xml','wbxml')).read()


# api.add_resource(SyncApp, '/funambol/dm')


def transfer(file_path):
    exec_cmd("java -jar wbxml.jar {}".format(file_path))


def exec_cmd(cmd_str):
    print(cmd_str)
    p = subprocess.Popen(cmd_str, shell=True)
    p.wait()


if __name__ == '__main__':
    __import__('shutil').rmtree('cache')
    app.run(debug=True)
