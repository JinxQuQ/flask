from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    print(request.args)
    print('破特=', request.args['port'])

    print('userId =', request.args['userId'])

    return "这是一个返回值"


app.run(debug=True)
