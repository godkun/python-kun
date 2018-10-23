# coding=utf-8
class Student():
    sum = 0

    # 构造函数
    # 类变量 实例变量
    def __init__(self, name, age):
        # 初始化对象的属性
        # 这是实例变量
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('当前学生总数:' + str(self.__class__.sum))

    # self就是固定的特征，必须在类中的函数参数中加一个self
    def do_homework(self):
        print('homework')

    # 装饰器 通过加一个classmethod装饰器来决定是类方法
    @classmethod 
    # cls是默认参数
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

# 不需要new
student1 = Student('杨昆1', 23)
Student.plus_sum()
student2 = Student('杨昆2', 24)
Student.plus_sum()