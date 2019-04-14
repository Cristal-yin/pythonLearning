# 一个完整的装饰器
import time
def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator # 对f1使用装饰器
def f1(func_name):
    print('This is a function ' + func_name)
@decorator 
def f2(func_name1, func_name2):
    print('This is a function ' + func_name1+ func_name2) 
@decorator
def f3(func_name1,func_name2,**kw):
       print('This is a function ' + func_name1+ func_name2)
       print(kw) 
 

f1('test func')
f2('haha','dd')
f3('a','v',a=2, c=3, b = 'adf')
# f = decorator(f1)
# f()