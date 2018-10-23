#coding=utf-8
import time
def decorator(func):
    # 可变参数 * 就代表可变参数
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f2(func_name):
    print('this is a' + func_name)
f2('5555')

# 这个就是装饰器了
# 不要改变原有函数的调用方式，不需要重新写一个函数非常好！！
@decorator
def f1(fun_name1, func_name2):
    print('this is a' + fun_name1 + func_name2) 
f1('222','333')

# 