from flask import Blueprint

blueprint = Blueprint("1", __name__, url_prefix="/1")


@blueprint.route('/1_1/')
def lhnews1():
    return "lhnews1"


@blueprint.route('/1_2/')
def lhnews2():
    return "lhnews2"
