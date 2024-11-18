def f(x, y, k):
    if x < y or k > 2:
        return 0
    if x == y and k <= 2:
        return 1
    if k == 2:
        return f(x - 2, y, k)
    return f(x - 2, y, k) + f(x // 2, y, k + 1)

print(f(40, 2, 0))
