import json
from flask import request, Response

# 所有科目列表
from flask_restful import Resource

from flask_restful_yds.druankao import CommonResponse


class AllCourseList(Resource):
    """
    所有课程列表
    """

    def post(self):
        req_json = request.json

        return CommonResponse(data={
            "courseList": {
                "1": "软件设计师",
                "2": "信息系统项目管理工程师",
            }
        }).to_json_response()


class ChapterList(Resource):
    """
    课程章节
    """

    def post(self, courseId):
        req_json = request.json

        if courseId == 1:
            return CommonResponse(data={
                    "courseId": courseId,
                    "chapterList": {
                        "1": "UML设计",
                        "2": "数据库设计",
                    }
            }).to_json_response()
        elif courseId == 2:
            return CommonResponse(data={
                    "courseId": courseId,
                    "chapterList": {
                        "1": "信息系统",
                        "2": "信息系统管理基础",
                    }
            }).to_json_response()


class ChapterQuestionList(Resource):
    """
    该章节下所有题目ID
    """

    def post(self, courseId, chapterId):
        req_json = request.json

        if courseId == 2 and chapterId == 1:
            return CommonResponse(data={
                {
                    "questions": [304, 305]
                }
            }).to_json_response()
        else:
            return CommonResponse(2001, "找不到对应的题目").to_json_response()
