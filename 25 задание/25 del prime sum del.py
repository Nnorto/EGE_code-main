def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
def dell(n):
    d = 2
    sp = []
    while d * d <= n:
        if n % d == 0:
            if prime(d):
                sp.append(d)
            if prime(n // d) and d * d != n:
                sp.append(n // d)
        d += 1
    return sp

k = 0
for n in range(550000+1, 10**10):
    s = sum(dell(n))
    if s % 10 == 7:
        k += 1
        print(n, s)
        if k == 5:
            break