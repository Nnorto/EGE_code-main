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
    n3 = f(n, 3)
    if n % 3 == 0:
        n3 = '1' + n3 + '02'
    else:
        ost = f((n%3)*4, 3)
        n3 += ost
    r = int(n3, 3)
    if r < 199:
        print(n)

