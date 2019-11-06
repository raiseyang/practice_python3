from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# 模拟返回新版本数据
mock_resp_check = """{"data":{"downStrategy":{"autoDownload":2,"downEcuInfos":[{"dst":{"ecuSVer":"HN4RJ5A_V0.10.41_190312","hash":"6eb99e750ef36a0b4bba72dd15bfa0bdd5ab2e9f2a1eba220bf40d4324d0aaab","packageType":1,"signFileHash":"4bc31b4cc82bb40b1bec8e6df1b8a8e6f218ffe0c97f422f08bb09a88b5989a8","signFileSize":3100,"signFileUrl":"http://otatest.gwm.com.cn:18800/download/package/65/fota/29c01771f1a24f6f91b9de2c4fe5be3b/MCU-sgin","size":269739,"verUrl":"http://otatest.gwm.com.cn:18800/download/package/65/fota/29c01771f1a24f6f91b9de2c4fe5be3b/MCU.bin"},"ecuPartNum":"7901100XNZ01A_MCU","src":{}}],"downloadExpire":5,"maxDownload":5,"netType":1,"releaseNote":"本次更新内容：\n1.系统优化\n2.问题修复"},"model":"EC01","sessionId":"1569208625315jprl","strategyId":416,"subModel":"NZA14B","upgradeStrategy":{"autoUpgrade":1,"batteryVoltage":9.0,"carSpeed":2,"disclaimer":"","ecusInfo":[{"dependencies":[],"dstVer":"HN4RJ5A_V0.10.41_190312","ecuPartNum":"7901100XNZ01A_MCU","ecuType":"HUT_MCU","partType":"HUT_MCU","srcVer":"HN4RJ5A_V0.10.36_190111","upgradeOrder":1}],"electricMotorSpeed":2,"engineSpeed":2,"fromTime":"0:00","gear":2,"isRollback":2,"matchPatterns":2,"maxUpgradeTimes":5,"minPower":30,"parkingStatus":2,"powerModel":1,"powerStatus":2,"toTime":"23:59","upgradeNote":"安装包已下载完成，是否立即升级？\n请您在升级期间不要使用车辆，以免升级失败。"}},"msg":"成功","status":1000}"""
# 模拟返回注册数据
mock_resp_register = """{"status":1000,"msg":"成功","data":{"deviceId":"9a19814abdb763ee16f1d972f2c3454c","secret":"5cba4864799558660825244955416f65"}}"""


class Check(Resource):
    def post(self):
        return mock_resp_check


class Register(Resource):
    def post(self):
        return mock_resp_register


api.add_resource(Check, '/v2/9a19814abdb763ee16f1d972f2c3454c/check')
api.add_resource(Register, '/v2/register')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
