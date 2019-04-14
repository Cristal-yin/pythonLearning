# 匿名函数
def add(x,y):
    return x+y

# print(add(1,2))
# 匿名函数 
f = lambda x,y: x + y
print(f(1,2))

# lambda 表达式
# lambda parameter_list:expression
# 不能再lambda里做赋值操作
# x, y x 大于y x 否则 y      x > y ? x : y
# 条件为真时返回的结果 if 条件判断 else条件为假时的返回结果

# 三元表达式
x = 2
y = 1
r = x if x > y else y
# print(r)