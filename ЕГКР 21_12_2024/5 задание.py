def ss3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1, 1000):
    n3 = ss3(n)
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        summa = sum(map(int, n3))
        s3 = ss3(summa)
        n3 += s3
    r = int(n3, 3)
    if r > 220 and r % 2 == 0:
        print(r)
        break