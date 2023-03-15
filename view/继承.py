from flask import Flask, render_template, views

app = Flask(__name__)


# 父类BaseView
# BaseView 与子类之间的关系如下：BaseView 提供了 dispatch_request 方法的实现，子类UserView继承了这个方法，不需要重新实现 dispatch_request；
# BaseView 定义了两个接口函数 get_template 和 get_data，子类UserView必须实现这两个方法。
#
class BaseView(views.View):
    def get_template1(self):
        # 抛出一个异常
        # 在 BaseView 中，get_template 和 get_data 的缺省实现是抛出错误 NotImplementedError，如果子类忘记定义了这两个方法，在运行时会报错。
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()

    # 在 BaseView 中，定义了方法 dispatch_request ()，调用 get_template () 获得模板的路径，调用 get_data () 获取模板的参数，
    def dispatch_request(self):
        data = self.get_data()
        template = self.get_template1()
        # 最后调用 render_template 根据模板路径 template 和模板参数 data 渲染输出。
        # 这里不用导入文件只需要写html的文件名就可以，使用 ** 来解码data字典数据
        return render_template(template, **data)

    # template规则  检查下面几点：
    #
    # 1、项目下面是否有templates文件夹，你的html文件是否放进了里面；
    # 2、templates文件夹是否和你运行的py文件在同一级目录；
    # 3、render_template('***.html')这里面的名字是否正确，别打错了；
    # 4、app = Flask(__name__, template_folder='templates', static_folder="****",static_url_path="****")


# 子类UserView，继承BaseView
class UserView(BaseView):
    # 在子类 UserView 中，get_template 返回模板路径为 ‘user.html’
    def get_template1(self):
        return 'user.html'

    # get_data 返回模板参数 name 和 gender
    def get_data(self):
        return {
            'name': 'zhangsan',
            'gender': 'male',
        }


# BaseView 中已经实现了视图类的 dispatch_request 方法，子类 UserView 继承了 BaseView 的 dispatch_request 方法，因此不需要再重新实现该方法。

app.add_url_rule('/user/', view_func=UserView.as_view('1'))
app.run(debug=True)
