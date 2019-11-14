## Jinja2
https://flask.palletsprojects.com/en/1.1.x/templating/

For Linux and Mac:
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```


For Windows cmd, use set instead of export:
```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

发布到Linux上：
```shell
# 1. 编译.whl文件
python setup.py bdist_wheel
# 2. 拷贝dist/*.whl文件到linux机器上
# 3. 创建venv虚拟环境，并激活虚拟环境
# 4. 安装flask web 安装包
pip install flaskr-1.0.0-py3-none-any.whl
# 安装waitress
pip install waitress
# 启动flask app[可能需要flask init-db]
waitress-serve --call 'flaskr:create_app'
```


```生成SECRET_KEY
You can use the following command to output a random secret key:

$ python -c 'import os; print(os.urandom(16))'

b'_5#y2L"F4Q8z\n\xec]/'
Create the config.py file in the instance folder, which the factory will read from if it exists. Copy the generated value into it.

venv/var/flaskr-instance/config.py
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
```

A detail view to show a single post. Click a post’s title to go to its page.

Like / unlike a post.

Comments.

Tags. Clicking a tag shows all the posts with that tag.

A search box that filters the index page by name.

Paged display. Only show 5 posts per page.

Upload an image to go along with a post.

Format posts using Markdown.

An RSS feed of new posts.