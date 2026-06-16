def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x == 15:
        return 0
    return f(x - 2, y) + f(x - 5, y) + f(x // 3, y)


print(f(46, 22) * f(22, 5))