def prime(n):
    for d in range(2, int(n**0.5) +1):
        if n % d == 0:
            return False
    return True

def maxprime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if not prime(n // d):
                return n // d
    return 0

f = 0
for n in range(450000+1, 10**10):
    if maxprime(n) != 0:
        f += 1
        print(n, maxprime(n))
        if f == 6:
            break