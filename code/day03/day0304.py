# 闭包
# 闭包的意思 保护现场 并不只返回一个函数
# 函数 知识一段可执行的代码，并不可以实例化 不是对象
# python一切皆对象


# 把一个函数当做另外一个函数的参数

def a():
    pass
# 闭包 = 函数 + 环境变量（函数定义时候外部变量 且不是全局变量）
# print(type(a))
def curve_pre():
    a = 25
    b = 2
    c = 50
    def curve(x):
        return a*x*2 + b*x + c
    return curve # 相当于返回一个函数

a = 10
f = curve_pre()
print(f(3))
    
