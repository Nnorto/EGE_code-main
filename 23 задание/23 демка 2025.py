def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x - 2, y) + f(x // 2, y)

print(f(38,16)*f(16, 2))
