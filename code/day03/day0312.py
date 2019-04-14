# filter 过滤

list_x = [1,0,1,0,0,1]
# 将数值为0 的数过滤掉
list_u = ['a','B','c','F','e']


r = filter(lambda x:True if x == 1 else False,list_x)
print(list(r))