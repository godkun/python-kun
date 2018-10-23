# coding=utf-8
class Student():
    name = ''
    age = 0

    # 构造函数
    def __init__(self, name, age):
        # 初始化对象的属性
        # 这是类变量
        name = name
        age = age
        print('666')

    # self就是固定的特征，必须在类中的函数参数中加一个self
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

# 不需要new
student1 = Student('我', 39)
print(student1.name)
student1.print_file()