def f(x, y, k):

    if x > y or k > 1:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, k) + f(x + 2, y, k) + f(x *2, y, k+1) + f(x * 3, y, k+1)


print(f(1, 10, 0))