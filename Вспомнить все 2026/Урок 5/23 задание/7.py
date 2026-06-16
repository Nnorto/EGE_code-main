def f(x, y, posl, pred):
    if x == y and pred == 1:
        return 1
    if x > y:
        return 0
    return f(x + 2, y, 1, posl) + f(x + 3, y, 2, posl) + f(x * 3, y, 3, posl)

print(f(2, 21, 0, 0))


def f(x, y, posl, pred):
    if x == y and pred == 2:
        return 1
    if x > y:
        return 0
    return f(x + 2, y, 1, posl) + f(x + 3, y, 2, posl) + f(x * 3, y, 3, posl)

print(f(2, 21, 0, 0))