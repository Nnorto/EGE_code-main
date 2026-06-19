def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def dell(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i):
                d.add(i)
            if prime(n//i):
                d.add(n//i)
    if d:
        return min(d) + max(d)
    return 0

for n in range(7_800_001, 10**10):
    m = dell(n)
    if m > 100_000 and str(m) == str(m)[::-1]:
        print(n, m)