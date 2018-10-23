#coding=utf-8
import time
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

# 这个就是装饰器了
def f1():
    print('this is a')


f = decorator(f1)

f()

# wrapper被decorator装饰了，但是并没有和f1关联在一起