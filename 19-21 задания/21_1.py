
def f(x, y, p):
    if x + y >= 91 and p == 3:
        return True
    if x + y < 91 and p == 3:
        return False
    if x + y >= 91:
        return False
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x * 4, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 4, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 4, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 4, p + 1)

for i in range(1, 86):
    if f(5, i, 0):
        print(i)