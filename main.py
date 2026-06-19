def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if str(x)[2] >str(x)[1]:
        s = str(x)[0]
        d = str(x)[1]
        e = str(x)[2]
        swap = s+e+d
        return f(x + 1, y) + f(int(swap), y)
    return f(x + 1, y)
print(f(100, 150))