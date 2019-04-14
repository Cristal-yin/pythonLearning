# 装饰器 只是一种模式
# 特性 注解

import time 
def f1():
    # print(time.time()) 
    print('This is a function1')

# unix 时间戳
# 
f1()
# 对修改时封闭的，对扩展是开放的
def f2():
    # print(time.time()) 
    print('This is a function2')

# 函数的参数也可以是函数
def  print_current_time(func):
    print(time.time())
    func()
    
print_current_time(f1)
print_current_time(f2)
# 缺点 ： 