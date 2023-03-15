from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)


# 定义一个用来检查登录的装饰器，即check_login
# 装饰器 check_login 本质是一个函数，它的输入是一个函数 original_function，它的输出也是一个函数 decorated_function。
def check_login(original_function):
    # original_function 是原先的处理 URL 的视图函数，它不包含检查登录的功能逻辑
    # 使用 functools.wraps (original_function) 保留原始函数 original_function 的属性
    @wraps(original_function)
    # decorated_function 是在 original_function 的基础上进行功能扩充的函数，它首先检查是否已经登录，如果已经登录则调用 original_function，如果没有登录则返回错误。
    def decorated_function(*args, **kwargs):
        user = request.args.get("user")

        # 检查请求中的参数 user 是否为 ‘zhangsan’，如果 user 等于 ‘zhangsan’，表示用户已经登录，则调用 original_function，否则返回 ‘请先登录’
        if user and user == 'zhangsan':
            return original_function(*args, **kwargs)
        else:
            return '请先登录'

    return decorated_function


# decorators = [check_login] 设定视图类的装饰器，当访问 /page1 时，首先执行检查登录，然后再执行原始的功能。
class Page1(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page1'


class Page2(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page2'


#
app.add_url_rule(rule='/page1', view_func=Page1.as_view('1'))
app.add_url_rule(rule='/page2', view_func=Page2.as_view('2'))
app.run(port=80, debug=True)
