import re

a = 'C0C++0Java4C#8Python9Javascript'

r = re.findall('\d',a)

# 把a字符串中的数字全部提取出来
# print(r)
# 'Python' 普通字符 '\d' 元字符
# 正则表达式就是有这两种字符组成的
# \d 等价于 [0-9]

str = re.findall('\D',a)

print(str)