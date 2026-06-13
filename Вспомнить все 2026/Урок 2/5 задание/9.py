from string import printable


def ss(n):
    s = ''
    while n > 0:
        s += printable[n % 12]
        n //= 12
    return s[::-1]

for n in range(1, 1000):
    n12 = ss(n)
    if n % 12 == 0:
        n12 += n12[-3:]
    else:
        ost = n % 12
        ost *= 12
        ost12 = ss(ost)
        n12 += ost12

    r = int(n12, 12)
    if r <= 300:
        print(r)