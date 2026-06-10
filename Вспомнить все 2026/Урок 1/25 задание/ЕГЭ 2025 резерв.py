def prime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0: return False
    return n > 1

def dell(n):
    d = set()
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            if prime(i) and str(i).count('2') == 1:
                d.add(i)
            if prime(n//i) and str(n//i).count('2') == 1:
                d.add(n//i)
    d = list(d)
    if len(d) == 2:
        if d[0] * d[1] == n:
            return max(d)
    if len(d) == 1:
        if d[0] * d[0] == n:
            return max(d)
    return 0
for n in range(6_651_220+1, 6_651_520):
    d = dell(n)
    if d:
        print(n, d)