闭包 = 函数 + 环境变量
说白了，就是用函数这个包，把变量包起来

def curve_pre():
    a = 2
    def curve(x):
        return a*x*x
    return curve

a = 10

f = curve_pre()

print(f(2))