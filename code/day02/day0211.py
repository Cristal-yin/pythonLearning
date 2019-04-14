import re 
a = 'PythonPythonPythonPythonPython'
# 4-8
# r = re.findall('(Python){3}',a)
# print(r)
# ()是一个且关系 []是一个或关系

language = 'PythonC#\nJAva'
# 忽略大小写 re.I
r = re.findall('c#.{1}',language, re.I | re.S)
print(r)
# . 表示c除了 \n 以外其他的字符
# re.S 忽略 . 的功能