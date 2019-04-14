# reduce 
# 连续的计算 连续调用lambda表达式
from functools import reduce
list_x = ['1','2','3','4','5','6','7','8']
# 每一次lambda表达式运算结果作为下一次的输入
r = reduce(lambda x,y:x+y,list_x,'aaa')
print(r)

# map/reduce 编程模型 映射归约 并行计算
# 函数式编程