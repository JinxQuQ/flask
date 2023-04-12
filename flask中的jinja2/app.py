# app1.py 是 Flask 程序，将渲染后的模板返回给浏览器；templates 是存放模板的目录，它和 app1.py 位于相同的目录；templates/index.html 是模板文件。
from flask import Flask, render_template
# 从模块 flask 中导入函数 render_template，该函数将 jinja2 模板渲染为 html
app = Flask(__name__)


@app.route('/')
def index():
    # 编写路径 / 的处理函数 index()，调用 render_template，对模板 templates/index.html 进行渲染
    # render_template 包含有两个命名参数: name 和 age，{{ name }} 被替换为 name，{{ age }} 被替换为 age
    return render_template('index.html', name='tom', age=10)


app.run(debug=True)
