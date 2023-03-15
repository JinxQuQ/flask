#!/usr/bin/python3
from flask import Flask
from flask import request

app = Flask(__name__)


def echo(key, value):
    print('%-8s = %s' % (key, value))
#   %-10s是占位符，意思是不超过10位就空白补齐，超过十位就正常输出
#   %s作用是将对象传到str()方法中进行处理，输出字符串


@app.route('/query')
# 定义路径 /query 的处理函数 query()；
def query():
    # 打印 request 对象中和 URL 相关的属性；
    echo('url', request.url)
    echo('base_url', request.base_url)
    echo('host', request.host)
    echo('host_url', request.host_url)
    echo('path', request.path)
    echo('full_path', request.full_path)
    print()
    # URL 中的查询参数保存在 request.args 中，打印查询参数 userId 的值。
    print(request.args)
    print('userId = %s' % request.args['userId'])
    return 'hello11111111'


if __name__ == '__main__':
    app.run(port=80)
