import re

s = 'life is short,i use python'

# 两种方法结果是一样的
# r = re.search('life(.*)python',s)
r = re.findall('life(.*)python',s)

print(r)
# group(0) 永远获取完整匹配结果 
# r.group(0,1,2)
# r,groups()