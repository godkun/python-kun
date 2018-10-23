from functools import reduce
j = [1,2,3,4,5,6,7]
r = reduce(lambda x,y:x+y ,j)

print(r)