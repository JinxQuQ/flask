from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

user = "root"
password = "123456"
database = "school"
# 字符串中的 “mysql+pymysql” 表示：数据库类型是 mysql，使用 pymysql 作为访问 mysql 的底层 API
uri = "mysql+pymysql://%s:%s@localhost:3306/%s" % (user, password, database)
app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students1'
    studentnum = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(255))
    studentage = db.Column(db.Integer)

    def dump(self):
        print(self.studentnum, self.studentname, self.studentage)


def create_table():
    with app.app_context():
        db.drop_all()
        db.create_all()


def insert_students():
    jinx = Student(studentnum=97, studentname='jinx', studentage=17)
    db.session.add(jinx)
    db.session.commit()

    lux = Student(studentnum=8527, studentname='lux', studentage=23)
    jax = Student(studentnum=12138, studentname='jax', studentage=42)
    db.session.add_all([lux, jax])
    db.session.commit()


def query_students():
    print('查询所有的学生')
    students = Student.query.all()
    for student in students:
        student.dump()
    print()

    print('查询所有年龄是 17 岁的学生')
    students = Student.query.filter_by(studentage=17)
    for student in students:
        student.dump()
    print()

    print('查询第一个年龄是 17 岁的学生')
    students = Student.query.filter_by(studentage=17)
    student = students.first()
    student.dump()
    print()

    print('查询姓名是 jinx 并且年龄是 17 岁的学生')
    students = Student.query.filter_by(studentage=17, studentname='jinx')
    for student in students:
        student.dump()
    print()


def update_students():
    students = Student.query.filter_by(studentname='jinx')
    students.update({'studentname': 'Jinxxxx'})
    db.session.commit()


def delete_students():
    students = Student.query.filter_by(studentname='lux')
    students.delete()
    db.session.commit()


command = sys.argv[1]
if command == "create":
    with app.app_context():
        create_table()

if command == "insert":
    with app.app_context():
        insert_students()

if command == "query":
    with app.app_context():
        query_students()

if command == "update":
    with app.app_context():
        update_students()

if command == "delete":
    with app.app_context():
        delete_students()


