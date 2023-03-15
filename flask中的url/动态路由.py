from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def get_user(name):
    return "my name is %s" % name


@app.route('/age/<int:age>')
def get_age(age):
    return "my age is %d" % age


@app.route('/money/<float:money>')
def get_MONEY(money):
    return "i have a lot of money almost %.2f" % money


app.run(port=80)

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/user/<name>')
# def show_user(name):
#     return 'My name is %s' % name
#
#
# if __name__ == '__main__':
#     app.run()
