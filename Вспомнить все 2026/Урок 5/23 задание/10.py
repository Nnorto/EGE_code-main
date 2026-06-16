def f(x, y, ch):
    if x == y and ch <= 4:
        return 1
    if x > y:
        return 0
    if x % 2 == 0:
        ch += 1
    return f(x + 1, y, ch) + f(x + 3, y, ch) + f(x * 2, y, ch)

print(f(1, 17, 0))

def f(x, y, ch):
    if x == y and ch <= 4:
        return 1
    if x > y:
        return 0
    if x % 2 == 0:
        return f(x + 1, y, ch) + f(x + 3, y, ch) + f(x * 2, y, ch + 1)
    else:
        return f(x + 1, y, ch + 1) + f(x + 3, y, ch + 1) + f(x * 2, y, ch + 1)

print(f(1, 17, 0))

