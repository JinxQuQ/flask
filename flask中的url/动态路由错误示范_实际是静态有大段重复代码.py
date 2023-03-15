from flask import Flask

app = Flask(__name__)


# https://blog.csdn.net/qq_44864833/article/details/122423539
@app.route('/user/xiaoming')
def xiaoming():
    return "mynameisxiaoming"


@app.route('/user/xiaohong')
def xiaohong():
    return "mynameisxiaohong"


@app.route('/user/xiaowang')
def xiaowang():
    return "mynameisxiaowang"


if __name__ == '__main__':
    app.run()
