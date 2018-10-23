# coding=utf-8
class Student():
    name = ''
    age = 0

    # self就是固定的特征，必须在类中的函数参数中加一个self
    def print_file(self):
        print('name: ' + name)
        print('age: ' + str(age))

# 不需要new
student = Student()

student.print_file()