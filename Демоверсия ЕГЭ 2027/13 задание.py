def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    s, d, e = str(x)
    if d < e:
        res = s+e+d
        return f(x + 1, y) + f(int(res), y)
    return f(x + 1, y)
print(f(100, 141))