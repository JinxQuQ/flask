from flask import Blueprint

# 创建一个名为 ‘products’ 的蓝图，该蓝图中页面的 URL 前缀为 /products
blueprint = Blueprint('products', __name__, url_prefix='/products')


@blueprint.route("/car")
# 将路径 /car/ 和函数 car_products 关联
def car_products():
    return "汽车产品版块"


@blueprint.route("/baby")
# 将路径 /baby/ 和函数 baby_products 关联
def baby_products():
    return "婴儿产品版块"
