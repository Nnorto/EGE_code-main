def f(x, y, flag):
    if x == y:
        return 1
    if x < y:
        return 0
    if flag == True:
        return f(x - 2, y, False)
    return f(x - 2, y, False) + f(x // 2, y, True)

print(f(50, 1, False))