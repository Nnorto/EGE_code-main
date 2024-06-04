def f(n):
    s = ''
    while n > 0:
        if n % 12 == 10:
            s = 'A' + s
        if n % 12 == 11:
            s = 'B' + s
        else:
            s = str(n % 12) + s
        n //= 12
    return s



for n in range(1, 100000):
    n2 = f(n)
    if n % 12 == 0:
        n2 += n2[-3:]
    else:
        n2 += f((n % 12)*12)

    r = int(n2, 12)
    if r <= 1380:
        print(r)

# or
print("*****")
def dv(n):
    res = []
    while n > 0:
        res = [str(n % 12)] + res
        n = n // 12
    return res

for n in range(1,1380):
    n12 = dv(n)
    if n % 12 == 0:
        n12 = n12 + n12[-3:]
    else:
        ost = (n % 12)*12
        ost12 = dv(ost)
        n12 = n12 + ost12
        nstr = ''.join(n12)
        r = int(nstr, 12)
        if r <= 1380:
            print(r)

