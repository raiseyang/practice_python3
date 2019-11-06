import json
import time
from flask import Flask, request, Response
from flask_restful import Resource, Api

from flask_restful_yds.druankao import CommonResponse
from flask_restful_yds.druankao.course import AllCourseList, ChapterList, ChapterQuestionList
from flask_restful_yds.druankao.question import Question

app = Flask(__name__)
api = Api(app)

user = {
    "123": "abc"
}


class Login(Resource):
    """
    登录
    """

    def post(self):
        req_json = request.json
        if req_json['username'] == "123" and req_json['password'] == "abc":
            # print("开始睡5秒")
            print(time.time())
            # time.sleep(5)
            # https://www.cnblogs.com/lyg-blog/p/9332609.html
            return CommonResponse(
                data={
                    "token": "1213456778"
                }).to_json_response()
        else:
            return CommonResponse(1002, "用户名和密码不能为null").to_json_response()


class Register(Resource):
    """
    注册
    """

    def post(self):
        req_json = request.json
        if len(req_json['username']) > 0 and len(req_json['password']) > 0:
            print("register %s", time.time())
            # 如果用户名已经占用
            if req_json['username'] in user:
                return CommonResponse(1001, "用户名已存在").to_json_response()

            user[req_json['username']] = req_json['password']
            print(user)
            return CommonResponse().to_json_response()
        else:
            return CommonResponse(1002, "用户名和密码不能为null").to_json_response()


# 用户信息
class UserInfo(Resource):
    def post(self):
        req_json = request.json
        token = req_json['token']
        if token == '1213456778':
            return CommonResponse(
                data={
                    "avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571155617147&di=d5748a210bb83a83944b46573d033fd4&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01ffaa593fc51ea8012193a3c0c057.png",
                    "nickname": "hello",
                    "activeCourse": -1
                }
            ).to_json_response()
        else:
            return CommonResponse(1003, "token不正确").to_json_response()


# api.add_resource(login, '/<string:count>')
api.add_resource(Login, '/user/login')
api.add_resource(Register, '/user/register')
api.add_resource(UserInfo, '/user/userInfo')
api.add_resource(AllCourseList, '/course/allCourseList')
api.add_resource(ChapterList, '/course/chapterList/<int:courseId>')
api.add_resource(ChapterQuestionList, '/course/chapterQuestion/<int:courseId>/<int:chapterId>')
api.add_resource(Question, '/question/<int:questionId>')


def test():
    common_response = CommonResponse(1000, "success")
    common_response.data = {
        "token": "1213456778"
    }
    print(json.dumps(common_response, default=lambda o: o.__dict__))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    # test()
