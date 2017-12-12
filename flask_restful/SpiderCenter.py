import time
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ApkDetail(Resource):
    def post(self, product_id, device_id):
        request_body = request.get_json()  # application/json
        print('ApkDetail', request_body)
        # 校验request_body

        print(product_id, device_id)

        # time.sleep(10)
        return {
            "status": 1000,
            "msg": "success",
            "data": [
                {
                    "appIcon": "http://c16.eoemarket.net/app0/110/110631/icon/1822248_480.png",
                    "appName": "饿了么",
                    "packageName": "me.ele",
                    "versionCode": 204,
                    "versionName": "7.23.1",
                    "downUrl": "http://d2.eoemarket.com/app0/110/110631/apk/1822248.apk?channel_id=426",
                    "downSize": 27168017,
                    "description": "【一路热送】—饿了叫【热】的饿了么，这个冬天不再冷！【大牌代言】科比,王祖蓝 联合代言，邀您畅享王者盛宴，美食、红包尽享全场！",
                    "simpleDesc": "叫外卖，用饿了么！外卖神器！",
                    "downTimes": "30万次",
                    "publishTime": 1500720601,
                    "sortNum": 1,
                    "downMd5": "DCEFA919D8849FBF0668279F5CB995A5"
                },
                {
                    "appIcon": "http://c13.eoemarket.net/app0/787/787247/icon/1803587_480.png",
                    "appName": "UC头条",
                    "packageName": "com.uc.infoflow",
                    "versionCode": 235,
                    "versionName": "3.2.0.320",
                    "downUrl": "http://d2.eoemarket.com/app0/787/787247/apk/1803587.apk?channel_id=426",
                    "downSize": 8_430_951,
                    "description": " UC头条是一款为兴趣而生的品质阅读资讯APP，由UC浏览器团队潜心打造，聚合海量优质新闻数据源，依托大数据技术，根据你的兴趣推荐符合口味的资讯内容。带你从兴趣出发，发现专属于自己的阅读乐趣。「懂你的新闻推荐」· 早间美女新闻播报，收听最热点新闻· 十年技术积累,读懂你的阅读兴趣· 智能学习算法,用得越多,Ta越贴心「海量优质内容」· 签约过千",
                    "simpleDesc": "最懂你的资讯阅读推荐平台！  ",
                    "downTimes": "12万次",
                    "publishTime": 1504720601,
                    "sortNum": 2,
                    "downMd5": "D52533E5C4CC845D86F167AF09622464"
                }
            ]
        }


class Packages(Resource):
    def post(self, product_id, device_id):
        request_body = request.get_json()  # application/json
        print(request_body)
        # 校验request_body

        print(product_id, device_id)
        return {
            "status": 1000,
            "msg": "success",
            "data": {
                "packageName": [
                    "com.uc.infoflow",
                    "me.ele"
                ]
            }
        }


class Report(Resource):
    def post(self, product_id, device_id):
        request_body = request.get_json()  # application/json
        print('Report', request_body)
        # 校验request_body

        print(product_id, device_id)
        return {
            "status": 1000,
            "msg": "success",
            "data": None
        }


class Register(Resource):
    def post(self, product_id):
        request_body = request.get_json()  # application/json
        print('Register', request_body)
        # 校验request_body

        print(product_id)
        return {
            "status": 1000,
            "msg": "success",
            "data": {
                "deviceId": "adfadfddsswwwqqazsdddd",
                "deviceSecret": "adfadfddsswwwqqazsdddd"
            }
        }


# /product/1/2/app/checkAllApp
api.add_resource(Packages, '/product/<string:product_id>/<string:device_id>/app/checkAllApp')
# api.add_resource(Packages, '/<string:product_id>/<string:device_id>')
api.add_resource(ApkDetail, '/product/<string:product_id>/<string:device_id>/app/checkNewApp')

api.add_resource(Report, '/product/<string:product_id>/<string:device_id>/app/reportAppResult')

api.add_resource(Register, '/register/<string:product_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
