def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x - 1, y) + f(x // 2, y)
print(f(40, 15)*f(15, 6))