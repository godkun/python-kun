# coding=utf-8


def fun(x, y):
    r1 = x * 3
    r2 = y * 2
    # 返回元祖
    return r1, r2

re = fun(2, 3)

# 使用有意义的变量名称来接受函数的返回值
var1, var2 = fun(1,2)
# 序列解包
print(var1, var2)
# 不要使用特定序号来获取特定数据
print(re[0], re[1])
print(type(re))
