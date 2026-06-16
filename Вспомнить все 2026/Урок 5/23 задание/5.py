def f(x, y, flag):
    if x == y and flag:
        return 1
    if x > y:
        return 0
    if x == 19 or x == 14:
        flag = True
    return f(x + 3, y, flag) + f(x + 5, y, flag) + f(x * 2, y, flag)

print(f(4, 31, False))



