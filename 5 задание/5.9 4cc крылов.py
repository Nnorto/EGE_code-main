def f(num, sist):
    if n == 0:
        return '0'
    else:
        res = ""
        while num > 0:
            res = str(num % sist) + res
            num //= sist
        return res


for n in range(1000):
    n4 = f(n, 4)
    if n % 4 == 0:
        n4 = n4 + n4[-2:]
    else:
        ost = f((n%4)*2, 4)
        n4 += ost
    r = int(n4, 4)
    if r < 300:
        print(n)

