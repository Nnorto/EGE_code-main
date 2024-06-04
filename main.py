def ss(n, k):
    s = ''
    while n > 0:
        if n % 12 == 10:
            s = 'A' + s
        elif n % 12 == 11:
            s = 'B' + s
        else:
            s = str(n % k) + s
        n //= k
    return s

for n in range(1, 10000):
    n12 = ss(n, 12)
    if n % 12 == 0:
        n12 += n12[-3:]
    else:
        n12 += ss((n % 12)*12, 12)
    r = int(n12, 12)
    if r <= 1380:
        print(r)

