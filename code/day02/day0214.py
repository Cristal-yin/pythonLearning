import re


s = '8C3721D86'

r = re.match('\d',s)
print(r.span()) # 返回匹配的位置
# match尝试从首字母开始匹配 首字母不满足则返回None
r1 = re.search('\d',s)
print(r1.group())

# search 搜索整个字符串一旦有则返回