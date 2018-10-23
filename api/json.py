#coding=utf-8
import json

json_str = '{ "name": "kun", "age":"23"}'

st = json.loads(json_str)
print(type(st))
# 这是字典
print(st)


