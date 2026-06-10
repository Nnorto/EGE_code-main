def prime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0: return False
    return n > 1

def S(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i):
                d.add(i)
            if prime(n//i):
                d.add(n//i)

    if d:
        return sum(d)

    return 0


for n in range(550_001, 550_101):
    s = S(n)
    if s and s % 7 == 0:
        print(n, s)