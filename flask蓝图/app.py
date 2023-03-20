from flask import Flask
# 导入模块 news.py，在 news.py 中定义了一个蓝图对象 news.blueprint
import news
# 导入模块 products.py，在 products.py 中定义了一个蓝图对象 products.blueprint
import products


app = Flask(__name__)

# 在应用中注册蓝图对象 news.blueprint
app.register_blueprint(news.blueprint)
# 在应用中注册蓝图对象 products.blueprint
app.register_blueprint(products.blueprint)

app.run(debug = True)