def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if str(x).count('1') >= 1:
        ns = str(x).replace('1', '3')
        return f(x + 2, y) + f(int(ns), y)
    else:
        return f(x + 2, y)

print(f(10, 44))