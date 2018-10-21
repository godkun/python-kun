#coding=utf-8
for x in range(0, 10):
    print(x)

# 加个步数
for x in range(0, 10, 2):
    print(x)

for x in range(10, 0, -2):
    print(x)

a = [1,2,3,4,5,6,7,8]
for i in range(0, len(a), 2):
    print(a[i])

# 直接是[1,3,5,7]
b = a[0:len(a):2]
print(b)