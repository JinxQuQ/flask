from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 在安装flask_sqlalchemy时，需要在“文件-设置-python解释器”中手动搜索时将下划线改为短横杠
# 首先引入库 flask 和库 flask_sqlalchemy；
app = Flask(__name__)

# 然后对 SQLAlchemy 进行配置，设置如下参数：
# user：访问数据库的用户，假设是 root
# password：访问数据库的密码，假设是 123456
# database：数据库名称
# uri：SQLAlchemy连接数据库的字符串
user = 'root'
password = '123456'
database = 'school'

# 在第 10 行，对 SQLAlchemy 进行配置，SQLALCHEMY_DATABASE_URI 配置的是连接数据库的字符串，在这个例子中，该字符串为：
# mysql+pymysql://root:123456@localhost:3306/school

# 该字符串包含有数据库类型、用户名、密码、数据库名等信息，含义如下：
#
# mysql+pymysql：数据库类型是 mysql，使用 pymysql 作为访问 mysql 的底层 API
# root：访问数据库的用户
# 123456：访问数据库的密码
# school：数据库名称
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 最后，创建 SQLAlchemy 对象 db。
db = SQLAlchemy(app)


# 建立表和类的映射关系：创建类 Student 继承于 db.Model，表示类 Student 用于映射数据库中的表；
class Student(db.Model):
    # 设定 __tablename__ 为 students，表示将类 Student 映射到数据库中的表 students。
    __tablename__ = 'students'
    # 建立属性和字段的映射关系：射 sno 到表 students 的字段 sno，类型为整数 (db.Integer)，primary_key=True 表示该字段是主键；
    sno = db.Column(db.Integer, primary_key=True)
    # 映射 name 到表 students 的字段 name，类型为整数 (db.String);
    name = db.Column(db.String(255))
    # 映射 age 到表 students 的字段 age，类型为整数 (db.Integer)。
    age = db.Column(db.Integer)

# 使用 ORM 模型定义了关系数据库和对象的映射关系后，可以使用面向对象的语法访问数据库，如下所示：
with app.app_context():
    # 类 Student.query.all () 返回所有的学生，相当于使用 SQL 语句 “SELECT * from students” 查询所有的学生；
    students = Student.query.all()
for student in students:
    # 通过 student.sno、student.name、student.age 即可访问数据库中一条记录的相关字段。
    print(student.sno, student.name, student.age)
