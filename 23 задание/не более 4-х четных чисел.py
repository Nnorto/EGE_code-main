def f(x, y, kch):
    if x == y and kch <= 4:
        return 1
    if x > y:
        return 0
    if x % 2 == 0:
        return f(x + 1, y, kch) + f(x + 3, y, kch) + f(x * 2, y, kch + 1)
    else:
        return f(x + 1, y,  kch + 1) + f(x + 3, y,  kch + 1) + f(x * 2, y,  kch + 1)
print(f(1, 17, 0))
