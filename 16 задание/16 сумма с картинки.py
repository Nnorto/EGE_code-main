def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 != 0:
        return f(n - 1) - f(n - 2)
    if n > 2 and n % 2 == 0:
        s = 0
        for i in range(1, n):
            s += f(i)
        return s


print(f(15))