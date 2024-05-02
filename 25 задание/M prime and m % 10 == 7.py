def prime(n):
    if n >= 2:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True
    return False

def M(n):
    a = []
    d = 1
    m = 0
    while d * d < n:
        if n % d == 0:
            if prime(d):
                a.append(d)
            if prime(n // d):
                a.append(n // d)
        d += 1
    if d * d == n:
        if prime(d):
            a.append(d)

    mch = [x for x in a if x % 2 == 0]
    mnch = [x for x in a if x % 2 == 1]
    if len(mnch) > 0 and len(mch) > 0:
        m = abs(max(mch) - max(mnch))
    return m

c = 0

for n in range(100000, 10**10):
    m = M(n)
    if prime(m) and m % 10 == 7:
        print(n, m)
        c += 1
        if c == 4:
            break
