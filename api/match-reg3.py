#coding=utf-8
import re
s = 'A8C3721D86'

r = re.match('\d', s)
r2 = re.findall('\d', s)
r1 = re.search('\d', s)
print(r)
print(r1)
print(r2)