# 列表推导式
# 集合推导式
# map filter
# set 也可以被推导
# dict
a = {
    'wo': 12,
    'you': 13,
    'he': 14
}


# 需要调用items才能遍历字典
b = [key for key, value in a.items()]
print(b)