from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def post(self,count ):

        print(count)
        return '{"status":1000,"msg":"success","data":{"packageName":["com.uc.infoflow","me.ele"]}}'


api.add_resource(HelloWorld, '/<int:count>')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')
