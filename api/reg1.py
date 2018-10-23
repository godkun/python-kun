#coding=utf-8
import re

a = 'abc, acc, adc, aec, afc, ahc'
lanuage = 'jsc#pythonphpc#'

# lanuage = lanuage.replace('c#', 'go')

# r1 = re.findall('a[cf]c', a)

# r2 = re.sub('', '', lanuage, 0)
# c# 的位置会被这个函数的返回值替代
# value并不是字符串

# 这种替换在python中的意义非常重大
def convert(value):
    print(value)
    matched = value.group()
    print(matched)
    return '!!' + matched + '!!'

r4 = re.sub('c#', convert, lanuage)
# print(r1)
print(r4)
# print(lanuage)