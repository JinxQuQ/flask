from flask import Blueprint

# 创建一个蓝图对象，它包含 3 个参数：
#
# 第 1 个参数 ‘news’ 是蓝图的名称；
# 第 2 个参数 __name__ 是该蓝图所在的模块名，该蓝图的实现文件是 news.py，因此 __name__ 是 ‘news’；
# 第 3 个参数是指定页面的 URL 前缀为 ‘/news’，它会影响路由中路径的设置，请看下一段的注意。
blueprint = Blueprint('news', __name__, url_prefix='/news')


@blueprint.route("/society/")
# 将路径 /society/ 和函数 society_news 关联
def society_news():
    return "社会新闻版块"


@blueprint.route("/tech/")
# 将路径 /tech/ 和函数 tech_news 关联
def tech_news():
    return "IT 新闻板块"

# 注意：页面的绝对路径是 /news/society/ 和 /news/tech/，因为蓝图的 url_prefix 设置为 news，在蓝图内部，页面的相对路径是 /society/ 和 /tech/。
