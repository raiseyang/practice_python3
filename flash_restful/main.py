from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self, product_id, device_id):
        # product_id_1 = request.form['product_id']
        product_id_1 = request.get_json()  # application/json

        print('product_id_1', product_id_1)
        print('product_id', product_id)
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


api.add_resource(HelloWorld, '/<string:product_id>/<string:device_id>')

if __name__ == '__main__':
    app.run(debug=True)
