"""
Flask
Quickstart

url编码：url_for()
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page.'


# @app.route('/hello')
# def hello():
#     return 'Hello, World!'


@app.route('/hello/<name>')
def hello_world(name):
    return render_template('hello.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(debug=True, host='172.18.6.74')
    # app.run(debug=True)
