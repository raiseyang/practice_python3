"""
Flask
Quickstart
https://flask.palletsprojects.com/en/1.1.x/quickstart/

url编码：url_for()
"""

from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page.'


# @app.route('/hello')
# def hello():
#     return 'Hello, World!'


@app.route('/hello/<name>')
def hello_world(name):
    """
    使用html模板,注意可以传递参数给模板
    :param name:
    :return:
    """
    return render_template('hello.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    获取request post数据使用request.form['user']
    获取request get数据使用request.args.get('key','')
    :return:
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] == "123" and request.form['password'] == "abc":
            # 跳转到登录后的页面
            return
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/cookies')
def index():
    """
    读取cookies,使用request.cookies.get('username')
    :return:
    """
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.


@app.route('/cookies_save')
def index():
    """
    保存cookies,使用resp.set_cookie()
    :return:
    """
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/')
def index():
    """
    重定向到另一个endpoint
    :return:
    """
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    """
    404页面设置
    :param error:
    :return:
    """
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='172.18.6.74')
    # app.run(debug=True)
