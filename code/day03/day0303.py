from enum import IntEnum,unique

# IntEnum 限制每一个枚举类型是整数
# unique装饰器 限制不能有相同的值
@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4
    
# 23中设计模式  单例模式
    
