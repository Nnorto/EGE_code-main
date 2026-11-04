def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i) and prime(n // i):
                if str(i).count('16') == 1:
                    if str(n // i).count('16') == 1:
                        return i
    return 0

for n in range(1_103_285_717, 10**10):
    a = f(n)
    if a:
        print(n, a)