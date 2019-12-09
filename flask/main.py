import os
from flask import Flask, request, redirect, url_for, send_file, Response
from werkzeug import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['crt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "html"])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return filename


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(filename))
            return 'filename = ' + filename
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    return send_file(
        ".\\file_system\\1.pdf",
        # "E:\\workspace-raise\\python-workspace\\practice_python3\\flask\\file_system\\1.pdf",
        attachment_filename="1.pdf", as_attachment=True)


@app.route('/download_302', methods=['GET', 'POST'])
def download_302():
    print("""
    Response(headers={
        "Location": "http://127.0.0.1:5000/download_file"
    }, status="302")""")
    return Response(headers={
        "Location": "http://127.0.0.1:5000/download_file"
    }, status="302")


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return ".hello"


if __name__ == '__main__':
    app.run(debug=True)
