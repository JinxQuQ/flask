from flask import Flask, request
from functools import wraps  # 装饰器check_login用的

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


# 函数 page1 被装饰了 2 次，它的原始功能是处理 /page1 的页面逻辑，被 @check_login 装饰后，具备了检查登录的功能，
@app.route('/page1')
# 被 @app.route (’/page1’) 装饰后，绑定到路径为 /page1 的 URL，当访问 /page1 时，会访问 page1 函数
@check_login
def page1():
    return 'page1'


@app.route('/page2')
@check_login
def page2():
    return 'page2'


app.run(debug=True)
