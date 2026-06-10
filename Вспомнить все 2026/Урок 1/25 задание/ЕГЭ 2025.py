def prime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0: return False
    return n > 1

def dell(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i) and prime(n // i):
                if str(i).count('5') == 1 and str(n // i).count('5') == 1:
                    d.add(i)
                    d.add(n // i)
    if d:
        return max(d)
    return 0

for n in range(1_324_727+1, 1_325_327):
    d = dell(n)
    if d:
        print(n, d)