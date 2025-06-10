def ss3(n):
    s = ''
    while n > 0:
        s = str(n%3) +s
        n //= 3
    return s

for n in range(1, 10000):
    n3 = ss3(n)
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        ost = (n % 3)*5
        ost3 = ss3(ost)
        n3 += ost3
    r = int(n3, 3)
    if r >= 290:
        print(n)
        break
