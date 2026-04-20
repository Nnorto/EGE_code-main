def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def dell(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i) and prime(n // i):
                if str(i).count('3') == 2 and str(n // i).count('3') == 2:
                    d.add(i)
                    d.add(n // i)

    if d:
        return d
    return 0


kp = 0
for n in range(8_996_452 + 1, 10 ** 10):
    a = dell(n)
    if a:
        print(n, max(a))
        kp += 1
        if kp == 5:
            break
