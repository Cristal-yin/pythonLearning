# 类型
# 字典 枚举
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    # YELLOW = 3
    GREEN = 2
    BLACK = 3
    RED = 4
# 枚举里不能重复定义一个变量
# 但是标签名不同 数值可以相同 第二个就相当于第一个的别名

class Common():
    YELLOW = 1
# 看似是一个常量 实际上是一个变量
    
# print(VIP.YELLOW.value) # 枚举的值
# print(type(VIP.GREEN)) # 枚举的类型
# print(VIP['YELLOW']) # 枚举的名字
# 类里的变量可以更改  枚举里的变量不能更改

# 枚举的遍历
# for v in VIP:
    # print(v) # 枚举的名字
# 在遍历的时候 YELLOW_ALIES 不会被打印出来 因为是别名

# 可以将别名打印出来  名字：如下  类型:VIP.__members__.items()
# for v in VIP.__members__.items():
#     print(v)
    
# result = VIP.GREEN is  VIP.BLACK
# 枚举类型之间可以做 == & is  操作但是其他操作不可以 数值虽然相同但是枚举类型却不相同的
# 枚举值之间可以随意比较
# print(result)
# 两个枚举之间可以用等值比较

# 
a = 1
print(VIP(a))