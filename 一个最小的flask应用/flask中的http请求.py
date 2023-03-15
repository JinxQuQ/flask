# 3. Flask 中的 HTTP 方法 上面我们已经大概了解了什么是 HTTP 协议，简单来说就是客户端与服务端用来通信的协议，HTTP 协议中规定和很多 HTTP
# 方法来让我们根据不同的需求向服务端发起请求。下面我们通过一个具体的例子，说明如何在 Flask 中使用不同的 HTTP 方法：
#
from flask import Flask, request

app = Flask(__name__)


# 首先，导入类 flask中的url.Flask 和 flask中的url.request，request 封装了请求消息，可以获取请求的各种参数。

@app.route('/login', methods=['GET'])
def login():
    return '''
<form action="/check_login" method="POST">
  <p><input type="text" name="name"/></p>
  <p><input type="password" name="password"/></p>
  <p><input type="submit" value="submit"/></p>
</form>
'''


# 定义处理路径 /login 的函数 login，装饰器 @app.route(’/login’, methods = [‘GET’]) 表示使用 GET 方法处理路径 /login 的请求。
#
# 函数 login 返回一段用于登录的 HTML 表单，表单包括 2 个字段: name 和 password。在第 4 行，指定使用 POST 方法提交表单给服务端的 /check_login 页面。

@app.route('/check_login', methods=['POST'])
def check_login():
    name = request.form['name']
    password = request.form['password']
    if name == 'guest' and password == '123':
        return 'Login succeed'
    else:
        return 'Login failed'


# 定义处理路径 /check_login 的函数 check_login，装饰器 @app.route(’/check_login’, methods = [‘POST’]) 表示使用 POST 方法处理路径
# /check_login 的请求。
#
# 函数 check_login 根据请求的参数 name 和 password 是否正确，返回给用户相应的信息。在第 3 行，提取参数 name 的值，在第 4 行，提取参数 password 的值。如果 name 是
# guest，password 是 123，则返回登录成功消息，否则返回登录失败消息。

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9986)
