def f(n):
    if n < 10:
        return n
    else:
        m = f(n // 10)
        d = m % 10
        if m < d:
            return d
        else:
            return m


for n in range(100, 1000):
    if f(n) < 7:
        print(n, f(n))

# answ = 699 6