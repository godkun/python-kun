#coding=utf-8
import time

def f1():
    print(time.time())
    print('this is a function')

f1()


# 如果要在函数中加一个时间语句，不能手动去改变原有函数，应该是扩展一个函数或者一个类来完成功能

# 对修改是封闭的，对扩展是开发的。拒绝修改

def f2():
    print('this is a function')

