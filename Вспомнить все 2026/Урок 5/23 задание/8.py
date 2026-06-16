def f(x, y, a):
    if x == y:
        return 1
    if x > y:
        return 0
    if a == True:
        return f(x + 3, y, False) + f(x * 2, y, False)
    return f(x + 1, y, True) + f(x + 3, y, False) + f(x * 2, y, False)

print(f(4, 14, False))