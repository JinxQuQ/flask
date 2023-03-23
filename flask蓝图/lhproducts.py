from flask import Blueprint

blueprint = Blueprint("2",__name__,url_prefix="/2")

@blueprint.route('/2_1/')
def product1():
    return "pro1"

@blueprint.route('/2_2/')
def product2():
    return "pro2"