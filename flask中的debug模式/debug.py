from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def get_user(name):
    return "my name is %s" % name

app.run(debug=True)