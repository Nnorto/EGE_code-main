def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if str(x)[-2] < str(x)[-1]:
        swap = str(x)[0] + str(x)[-1] + str(x)[-2]
        return f(x + 1, y) + f(int(swap), y)
    return f(x + 1, y)

print(f(110, 154))