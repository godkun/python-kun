#coding=utf-8
class People():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)
    # 给方法或者变量加双下划线__ python就会认为这是私有的
    # 如果是私有的，就不能用实例对象去调用
    # __init__是特有的方法，可以在外部访问
    # 当变量前后都有双下划线__xx__ python都不会认为其实私有的
