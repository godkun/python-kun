# coding=utf-8
class Student():
    name = ''
    age = 0

    # 构造函数
    # 类变量 实例变量
    def __init__(self, name, age):
        # 初始化对象的属性
        # 这是实例变量
        self.name = name
        self.age = age
        print('666')

    # self就是固定的特征，必须在类中的函数参数中加一个self
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

# 不需要new
student1 = Student('我', 39)
# 打印对象和类的所有属性和方法
print(student1.__dict__)
print(Student.__dict__)