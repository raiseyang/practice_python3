import json
from flask import request, Response

# 所有科目列表
from flask_restful import Resource

from flask_restful_yds.druankao import CommonResponse


class Question(Resource):
    """
    具体的问题
    """

    def post(self, questionId):
        req_json = request.json

        if questionId == 305:
            return CommonResponse(
                data={
                    "question": {
                        "label": "19年5月",
                        "titleDesc": "下例数据整体管理过程组的是：_____",
                        "answerDesc": "A,XXXX | B,yyyy | C,IIII | D PPPP",
                        "rightKey": "B",
                        "answerAnalysis": "管理过程组：启动，计划，执行，控制与监督，收尾",
                        "level": "3"
                    }
                }).to_json_response()
