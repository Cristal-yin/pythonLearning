import re

a = 'C0C++0Java4C#8Python9Javascript'

# for in 
r = re.findall('Python',a)
if len(r) > 0:
    print('字符串中包含python')
else: 
    print('不包含')
