origin = 0
def go(step):
    global origin
    origin += int(step) # 只要在函数中给origin赋值 他就会定义一个新的变量
    return origin

print(go(2))
print(go(5))
print(go(6))