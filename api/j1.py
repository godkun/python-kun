# coding=utf-8
from j2 import People
# People 是 Student 的父类
class Student(People):
    # 给方法或者变量加双下划线__ python就会认为这是私有的
    # 如果是私有的，就不能用实例对象去调用
    # __init__是特有的方法，可以在外部访问
    # 当变量前后都有双下划线__xx__ python都不会认为其实私有的
    # sum = 0
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.__score = 0
    #     self.__class__.sum += 1

    def do(self):
        print(444)
    
st1 = Student('杨昆', 20)
print(Student.sum)
print(st1.name)
print(st1.age)
st1.get_name()