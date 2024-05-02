def ss5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


for n in range(10, 100000):
    s5 = ss5(n)
    if n % 25 == 0:
        s5 = s5[-3:] + s5
    else:
        os = ss5(n % 25)
        s5 = s5 + os
    res = int(s5, 5)
    if res > 10000:
        print(n)
        break
