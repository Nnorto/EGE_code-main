def f(x, y, c):
    if x == y and c == 1:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, 0) + f(x + 2, y, 0) + f(x * 2, y, c + 1) + f(x * 3, y, c + 1)


print(f(1, 20, 0))