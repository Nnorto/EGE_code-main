def f(n):
    global a
    a.append(n)
    if n > 0:
        d = (n % 10 + f(n // 10))
        a.append(d)
        return d
    else: return 0

for n in range(1, 1000):
    a = []
    f(n)
    if a[1] > 51:
        print(n, a)
        break

