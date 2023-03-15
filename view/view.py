from flask import Flask, views

app = Flask(__name__)


# 定义视图类 Index 用于处理路径为 / 的 URL，视图类 Index 继承于 Flask.views.View
class Index(views.View):
    # 定义方法 dispatch_request，该方法返回 ‘hello world’ 给客户端
    # dispatch_request 是固定方法
    def dispatch_request(self):
        return "hello"


# 将路径为 / 的 URL 和视图类 Index 绑定
app.add_url_rule(rule='/', view_func=Index.as_view('Index'))
app.run(debug=True)
