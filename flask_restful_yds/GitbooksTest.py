from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class BooksLinks(Resource):
    def post(self, count):
        print(count)
        return {
            "links": [
                'http://otlgsmu4m.bkt.clouddn.com/kotlin_book.zip'
            ]
        }


api.add_resource(BooksLinks, '/allBooks/<string:count>')

if __name__ == '__main__':
    app.run(debug=True,
            port=50001,
            host='127.0.0.1')
