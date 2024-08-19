def f(x, y, flag):
    if x == y and True:
        return 1
    if x > y:
        return 0
    if flag == 1:
        return f(x + 1, y, True) + f(x + 2, y, True)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(x * 2, y, True) + f(x * 3, y, True)
print(f(1, 10, False))


def f(x, y, k):
    if x > y:
        return 0
    if x == y and k == 1:
        return 1
    else:
        return f(x + 1, y, k) + f(x + 2, y, k) + f(x * 2, y, k + 1) + f(x * 3, y, k + 1)

print(f(1, 10, 0))
