import re

# s = 'abc,acc,adc,aec,afc,ahc'
 
# r = re.findall('a[^cf]c',s)
 
# print(r)
a = 'python111java%343php'

# r = re.findall('\w',a)
# print(r)
# \w 匹配的是单词字符

# 数量词 将整个单词提取出来
r = re.findall('[a-z]{3,6}',a)
# 贪婪 与 非贪婪
print(r) 

# * 号代表他前面的字符可以出现0次-无限多次
# + 号表示匹配1次-无限多次
# ？ 号表示匹配0次或者1次