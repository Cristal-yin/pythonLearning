# map 

a = 10
list_x = [1,2,3,4,5,6,7,8]
# list_y = [1, 4, 9, 16, 25, 36, 49, 64]
# def square(x):
#     return x * x

# map 会把集合里面的每一个元素都传到square里，并接收返回结果
# 把元集合里的每一个元素映射到新的集合里

# 通过lambda 表达式替换for循环 和square函数
r = map(lambda x: x *x, list_x)
print(list(r))