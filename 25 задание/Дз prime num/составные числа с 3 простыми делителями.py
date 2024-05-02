def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def comp_num(n):
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


count = 0
for x in range(2, 20_000 + 1):
    m = comp_num(x)
    if len(m) > 3:
        count += 1

print(count)

answ = "2362"