import json

json_str = '[{"name":"qiyue", "age":18},{"name":"cristal", "age":18}]'

# 反序列化 ：由字符串到某种数据结构的格式
student = json.loads(json_str)

print(student)
print(student[1]['name'])