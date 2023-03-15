from flask import Flask, request

app = Flask(__name__)


@app.route('/')
# 编写路径 / 的处理函数 root()，它读取文件 api.html，将内容返回给浏览器
def root():
    file = open('api.html', encoding='utf-8')
    return file.read()


# 客户端使用 POST 方法提交请求 /api/addUser，在 Flask 中，需要指明 methods 为 ‘POST’
@app.route('/api/addUser', methods=['POST'])
# 编写路径 /api/addUser 的处理函数 addUser()，打印 request.json 中的参数 name 和 age，返回给浏览器 ‘addUser OK’
def addUser():
    json = request.json
    print('JSON', json)
    print('name = %s' % json['name'])
    print('age = %s' % json['age'])
    return 'addUser OK'


if __name__ == '__main__':
    app.run(debug=True)


# https://www.5axxw.com/wiki/content/xr5unf
# 服务端收到将客户端发送的数据后，封装形成一个请求对象，在 Flask 中，请求对象是一个模块变量 flask.request，它包含了如下常用属性：
#
# 属性	说明
# method	当前的请求方法
# form	表单参数及其值的字典对象
# args	查询字符串的字典对象
# values	包含所有数据的字典对象
# json	如果 mimetype 是 application/json，这个参数将会解析 json 数据，如果不是则返回 None
# headers	http 协议头部
# cookies	cookie 名称和值的字典对象
# files	与上传文件有关的数据
