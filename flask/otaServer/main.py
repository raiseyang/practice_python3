import os
from flask import Flask, request, redirect, url_for, send_file, Response

app = Flask(__name__)

ClientConfigSync_resp = '{"msg":"","code":100000,"data":{"inventoryInstruction":{"ecuInstructionList":[{"validationKeyList":[{"didName":"F18C"},{"didName":"F1A0"},{"didName":"F1AA"},{"didName":"F1AB"},{"didName":"F1AE"},{"didName":"D0D0"},{"didName":"D0D1"}],"ecuAddress":"1201","ecuName":"DHU"}]},"configStatus":1}}';
PushClientConfig_resp = '{"msg":"","code":100000,"data":{"configStatus":1}}'
PushHMILanguageSetting_resp = '{"msg":"","code":100000}'
PushFOTASetting_resp = '{"msg":"","code":100000}'
PushAssignmentNotification_resp = '{"msg":"","code":100000}'
ReqDownload_resp = '{"msg":"","code":100000,"data":{"operationSequence":1,"ecuInstallationInstructions":[{"sblNotPresent":false,"expectedInstallationTime":9,"requiredPreparationTime":100000,"queuedRequest":false,"installationType":"UDS-STREAM-FLASH","fileSize":329,"softwareInstallationInstructions":[{"fileName":"8892365985A","sowfwareType":"SWBL","encryptionType":"00","fileSignature":"","url":"http://10.114.146.12:5001/vbfs/8892365985A.vbf","encryptInfo":"","flashGroupId":0,"fileSize":27943,"fileCheckSum":"261465C8","estimatedInstallationtime":10},{"fileName":"8893750315C","sowfwareType":"SWP2","encryptionType":"00","fileSignature":"","url":"http://10.114.146.12:5001/vbfs/8893750315C.vbf","encryptInfo":"","flashGroupId":0,"fileSize":307698,"fileCheckSum":"1C935EE5","estimatedInstallationtime":10},{"fileName":"8894301846A","sowfwareType":"SWP1","encryptionType":"00","fileSignature":"","url":"http://10.114.146.12:5001/vbfs/8894301846A.vbf","encryptInfo":"","flashGroupId":0,"fileSize":2855,"fileCheckSum":"600D68FF","estimatedInstallationtime":10}],"ecuAddress":"1201","downloadType":"Direct download","securityKey":"5TM61VdtYpJo+E/6n9/D9g==","busType":0,"installOrder":1,"validationKeys":[{"didValue":"3536313634373131","didName":"F18C"},{"didValue":"3831393430383734323441","didName":"F1A0"},{"didValue":"38383932323735353838","didName":"F1AA"},{"didValue":"","didName":"F1AB"},{"didValue":"03 8892365985 202041 8893750315 202043 8894301846 202041","didName":"F1AE"},{"didValue":"202020202020202020202020202020202020202020","didName":"D0D0"},{"didValue":"202020202020202020202020202020202020202020202020202020202020","didName":"D0D1"}]}],"targetECUNum":1,"bssId":"5830323233323030342D3331413446383835202020","clientVersion":"1","maximumParallelNum":6,"signatureCertificate":"","area1112SecurityCode":"FFFFFFFFFF","displayedversion":"303034202020202020202020202020202020202020202020202020202020"}}';
ReqAvailableAssignment_resp = '{"msg":"","code":100000,"data":{"availableAssignment":{"totalInstallationTime":160,"reason":"","newStatus":"任务下载成功","purpose":{"reCall":false,"safety":true,"cyberSecurity":false},"bssId":"5830323233323030342D3331413446383835202020","criticality":"false","description":"004","workshopInstallation":false,"downloadSize":329,"displayedVersion":"303034202020202020202020202020202020202020202020202020202020","name":"ZKOTA任务004-001","installationOrderId":"32657ec0d5c64086a80cbe96ce63c9ba"}}}';


@app.route('/openapi/gnds', methods=['GET', 'POST'])
def openapi():
    request_body = request.get_json()  # application/json
    print('request_body:', request_body)
    if request_body['methodName'] == 'ClientConfigSync':
        return ClientConfigSync_resp
    if request_body['methodName'] == 'PushClientConfig':
        return PushClientConfig_resp
    if request_body['methodName'] == 'ReqDownload':
        return ReqDownload_resp
    if request_body['methodName'] == 'ReqAvailableAssignment':
        return ReqAvailableAssignment_resp
    if request_body['methodName'] == 'PushHMILanguageSetting':
        return PushHMILanguageSetting_resp
    if request_body['methodName'] == 'PushFOTASetting':
        return PushFOTASetting_resp
    if request_body['methodName'] == 'PushAssignmentNotification':
        return PushAssignmentNotification_resp


    return ".hello"

# @app.route('/vbfs/8894301846A.vbf', methods=['GET', 'POST'])
# def download_file1():
#     return send_file(".\\vbfs\\8894301846A.vbf")

# @app.route('/vbfs/8892365985A.vbf', methods=['GET', 'POST'])
# def download_file2():
#     return send_file(".\\vbfs\\8892365985A.vbf")
# @app.route('/vbfs/8893750315C.vbf', methods=['GET', 'POST'])
# def download_file3():
#     return send_file(".\\vbfs\\8893750315C.vbf")


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return ".hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    # app.run(host='0.0.0.0',debug=True,ssl_context=('adhoc'))
    # app.run(host='0.0.0.0',debug=True,ssl_context=('cert.pem', 'key.pem'))
