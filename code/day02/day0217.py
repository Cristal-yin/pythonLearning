import json

student = [
    {'name':'qiyue', 'age':18, 'flag': False},
    {'name':'cristal','age':18}
]

#序列化 将object转化为str
#
json_str = json.dumps(student)

print(type(json_str))
print(json_str)