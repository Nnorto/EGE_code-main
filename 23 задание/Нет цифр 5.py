def f(x, y):
    if x == y:
        return 1
    if x % 10 == 5 or 50 <= x <= 59 or x > y:
        return 0
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 60))

def f(x, y):
    if x == y:
        return 1
    if x > y or '5' in str(x):
        return 0
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 60))

def f(x, y):
    if x == y:
        return 1
    if x > y or str(x).count('5') != 0:
        return 0
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 60))
