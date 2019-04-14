# 字典来代替switch
# 也可以使用if elif .....else来代替
day = 2
def get_sunday():
    return 'Sunday'
def get_Monday():
    return 'Monay'
def get_Sunday():
    return 'Sunnay'
def get_default():
    return 'Unknown'
switcher = {
    0 : get_sunday,
    1 : get_sunday,
    2 : get_sunday
}

day_name = switcher.get(day,get_default)() # 相当于defult

print(day_name)