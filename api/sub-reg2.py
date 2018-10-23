#coding=utf-8
import re
s = 'A8C3721D86'

def convert(value):
    print(value)
    # matched是字符串
    matched = value.group()
    if int(matched) >= 6:
        # 需要是字符串
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)
print(r)