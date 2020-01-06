"""
上传和下载文件
"""

import os
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

# 服务器上保存的目录
from python_excel_ import excel_read_, excel_write_
from terminal_ import cmd_shell_

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'file_system')
# 允许上传的格式
ALLOWED_EXTENSIONS = {'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

m_active_code_list = []
m_file_out = {
    "path": ""
}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    out_file = m_file_out['path']
    print("下载的文件路径：{}".format(out_file))
    return send_file(out_file, attachment_filename=os.path.basename(out_file), as_attachment=True)


@app.route('/uploaded_file', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'GET':
        file_name = request.args.get("filename")
        msg = request.args.get("msg")
        code_list = ""
        print("长度={}", len(m_active_code_list))
        for active_code in m_active_code_list:
            code_list += "{}\n".format(str(active_code))

        out_file_path = excel_write_.write(os.path.join(app.config['UPLOAD_FOLDER'], file_name),
                                           m_active_code_list)
        m_file_out['path'] = out_file_path
        print("目标文件：{}".format(m_file_out['path']))
        return '''
        <!doctype html>
        <title>Uploaded File Success</title>
        <h1>Uploaded File Success</h1>
        <a href="/download_file">下载文件</a>
        <p>msg={}</p>
        code={}
        '''.format(msg, code_list)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("request.method={}".format("upload_file"))
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            ids = excel_read_.read(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            m_active_code_list.clear()
            cmd = "./abup_sn --mid {} --ver ab01"
            for id in ids:
                code = cmd_shell_.exec_cmd(cmd.format(id).split(' '))
                m_active_code_list.append(str(code[0], encoding="utf8"))
            # 赋值给全局变量
            msg = "共生成{}个注册码".format(len(m_active_code_list))
            print(msg)
            return redirect(url_for('uploaded_file',
                                    filename=filename,
                                    msg=msg, ))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <ul>
        <li>MID列的判断标识为'ID'
        <li>激活码列的判断标识为'注册码'
    </ul>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='172.18.6.62', port=5001)
