import re
lanuage = 'PythonC#JavaC#'

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'
# 替换 re.sub  0 表示所有的C#都变成GO   2表示替换两个
r = re.sub('C#',convert,lanuage)
# language.replace('C#','GO')
#没有替换成功  因为字符串不可改变
#如果想变 需要重新设定一个字符串

# lanuage = lanuage.replace('C#','GO') # 这样是可以替换的  但是已经是另一个字符串了
print(r)

