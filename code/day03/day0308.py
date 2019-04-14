origin = 0
# 闭包的优点 不改变全局变量
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return pos
    return go

t = factory(origin)
print(t(2))
print(t(3))
print(t(5))
