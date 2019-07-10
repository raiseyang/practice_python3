from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '123' and password == '456':
            return 'true'
        else:
            return 'false'

    if request.method == 'GET':
        username = request.args.get('username', '')
        password = request.args.get('password', '')
        if username == '123' and password == '456':
            return 'true'
        else:
            return 'false'
    else:
        return 'use POST or GET.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')