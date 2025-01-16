def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def vsedel(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            if prime(d) and prime(n // d) and d != n // d:
                if prime(d + (n // d)):
                    return d + (n // d)
        d += 1
    return False
from fnmatch import fnmatch
for n in range(1, 10**7):
    s = vsedel(n)
    if s != False:
        if fnmatch(str(n), '13?45*8'):
            print(n, s)