def f(x, y):
    if x > y or x == 15 or x == 30:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(x ** 2, y)

print(f(3, 10) * f(10, 20) * f(20, 38))