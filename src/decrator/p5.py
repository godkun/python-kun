#coding=utf-8
import time
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f2():
    print('this is a')
# f2()

# 这个就是装饰器了
# 不要改变原有函数的调用方式，不需要重新写一个函数非常好！！
def f1():
    print('this is a')
f1()

# 