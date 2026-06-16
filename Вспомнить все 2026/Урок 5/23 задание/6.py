def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x == 28:
        return 0
    if x % 2 == 0:
        return f(x - 2, y) + f(x // 2, y)
    return f(x - 2, y) + f(x - 3, y)

print(f(98, 1))