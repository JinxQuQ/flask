#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
user = 'root'
password = '123456'
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)


# db.init_app(app)
# 创建 SQLAlchemy 对象，用于映射数据库表和对象

# flask_sqlalchemy 注册到app中有2种方法
# 方法一：直接在初始化的时候传app参数
# 初始化组件对象, 直接关联Flask应用
# db = SQLAlchemy(app)

# 方法二：使用db.init_app(app)方法
# # 先实例化，后关联app
# db = SQLAlchemy()
# # 初始化db,关联flask 项目
# db.app = app    # 这一步需先设置属性，很多老的教程都缺少这一步，导致连不上数据库
# db.init_app(app)


# 首先，建立表和类的映射关系：创建类 Student 继承于 db.Model，表示类 Student 用于映射数据库中的表
class Student(db.Model):
    # 设定 __tablename__ 为 students，表示将类 Student 映射到数据库中的表 students
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def dump(self):
        print(self.sno, self.name, self.age)


def create_table():
    print("testing")
    with app.app_context():
        db.drop_all()
        db.create_all()


def insert_students():
    tom = Student(sno=1, name='tom', age=12)
    db.session.add(tom)
    db.session.commit()

    jerry = Student(sno=2, name='jerry', age=11)
    mike = Student(sno=3, name='mike', age=11)
    db.session.add_all([jerry, mike])
    db.session.commit()


def query_students():
    print('查询所有的学生')
    students = Student.query.all()
    for student in students:
        student.dump()
    print()

    print('查询所有年龄是 11 岁的学生')
    students = Student.query.filter_by(age=11)
    for student in students:
        student.dump()
    print()

    print('查询第一个年龄是 11 岁的学生')
    students = Student.query.filter_by(age=11)
    student = students.first()
    student.dump()
    print()

    print('查询姓名是 jerry 并且年龄是 11 岁的学生')
    students = Student.query.filter_by(age=11, name='jerry')
    for student in students:
        student.dump()
    print()


def update_students():
    students = Student.query.filter_by(name='tom')
    students.update({'name': 'TOM'})
    db.session.commit()


def delete_students():
    students = Student.query.filter_by(name='mike')
    students.delete()
    db.session.commit()


# 例子程序是一个命令行程序，根据不同的命令行参数调用相应的功能函数
command = sys.argv[1]
if command == 'create':
    with app.app_context():
        print("傻B")
        create_table()
elif command == 'insert':
    with app.app_context():
        insert_students()
elif command == 'query':
    with app.app_context():
        query_students()
elif command == 'update':
    with app.app_context():
        update_students()
elif command == 'delete':
    with app.app_context():
        delete_students()
