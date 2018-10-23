#coding=utf-8
import time

def f1():
    print('this is a ')
f1()

def f2():
    print('this is b')
f2()

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)