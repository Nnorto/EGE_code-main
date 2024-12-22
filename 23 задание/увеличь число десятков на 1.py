def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if str(x)[-2] == '9':
        return f(x + 1, y) + f(x, y)
    return f(x + 1, y) + f(x + 10, y)
print(f(12, 36))

