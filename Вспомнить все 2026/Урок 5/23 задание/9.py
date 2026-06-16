def f(x, y, mp):
    if x == y and mp == True:
        return 1
    if x > y:
        return 0
    if mp == True:
        return f(x + 1, y, mp) + f(x + 2, y, mp)
    return f(x + 1, y, mp) + f(x + 2, y, mp) + f(x * 2, y, True) + f(x * 3, y, True)

print(f(1, 20, False))
