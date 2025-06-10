def prime(n):
    for d in range(2,  int(n**0.5) +1):
        if n % d == 0:
            return False
    return True

def dell(n):
    vd = []
    for d in range(2, int(n**0.5) +1):
        if n % d == 0:
            if prime(d) and prime(n//d) and d !=(n//d):
                if str(d).count('0') == 1 and str(n//d).count('0') == 1:
                    vd.append(d)
                    vd.append(n//d)
                    return vd
    return vd
kp = 0
for n in range(2_900_001, 10**10):
    a = dell(n)
    if len(a) == 2:
        print(n, max(a))
        kp += 1
        if kp == 5:
            break

