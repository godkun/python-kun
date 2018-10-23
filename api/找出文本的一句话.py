#coding=utf-8
import re
s = 'life is short, i use python'
# 加了()就是一个分组了
r = re.search('life(.*)python', s)
# group的目的是获取分组
# group(0)永远都是完整的匹配
print(r.group(1))
# (.*)就是一个组
print(r.groups(1))