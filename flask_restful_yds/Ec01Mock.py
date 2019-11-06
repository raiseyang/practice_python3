from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Register(Resource):
    def post(self):
        print(request.json)
        return {
            "status": 1000,
            "msg": "成功",
            "data": {
                "deviceId": "9a9eebd3018bb57c9321191fcf66ba01",
                "secret": "cae4f28584ad46845b0bafec6a9d5157"
            }
        }


class CheckVersion(Resource):
    def post(self, deviceId):
        print("deviceId = " + deviceId)
        print(request.json)
        return {
            "status": 1000,
            "msg": "成功",
            "data": {
                "sessionId": "1523253428191",
                "taskId": "134523523423",
                "strategyId": 26,
                "model": "wxlCarType",
                "subModel": "wxlSubCarType",
                "modelYear": "2018",
                "modelCode": "carTypeCode",
                "downStrategy": {
                    "maxDownload": 5,
                    "downloadExpire": 5,
                    "netType": 1,
                    "releaseNote": "1.系统优化",
                    "autoDownload": 1,
                    "downEcuInfos": [
                        {
                            "ecuPartNum": "ECU56432421001##AABFK-ECU1-FW",
                            "src": {
                                "packageType": 1,
                                "ecuSVer": "v1",
                                "verUrl": "http://imtt.dd.qq.com/16891/3FE2F242D1CEB5B351E0244DF9A2C3FD.apk",
                                "size": 4999510,
                                "hash": "3FE2F242D1CEB5B351E0244DF9A2C3FD"
                            },
                            "dst": {
                                "packageType": 1,
                                "ecuSVer": "v2",
                                "verUrl": "http://imtt.dd.qq.com/16891/05DD256AC616999F850CDCCBD6597701.apk",
                                "size": 9051505,
                                "hash": "05DD256AC616999F850CDCCBD6597701"
                            }
                        }
                    ]
                },
                "upgradeStrategy": {
                    "maxUpgradeTimes": 1,
                    "autoUpgrade": 1,
                    "fromTime": "",
                    "toTime": "",
                    "minPower": 30,
                    "upgradeNote": "",
                    "ecusInfo": [
                        {
                            "ecuPartNum": "partNumber_tbox",
                            "ecuType": 0,
                            "upgradeOrder": 1,
                            "srcVer": "v1.1",
                            "dstVer": "v1.3",
                            "dependencies": []
                        },
                        {
                            "ecuPartNum": "partNumber_mcu",
                            "ecuType": 0,
                            "upgradeOrder": 2,
                            "srcVer": "v2.3",
                            "dstVer": "v3.4",
                            "dependencies": []
                        }
                    ]
                }
            }
        }


class Hello(Resource):
    def post(self):
        return "Hello"


api.add_resource(Register, '/v1/register')
api.add_resource(CheckVersion, '/v1/<string:deviceId>/check')
api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True,
            port=50001,
            # host='172.16.30.32')
            host='0.0.0.0')
