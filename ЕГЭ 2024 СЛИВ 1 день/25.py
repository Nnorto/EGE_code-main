def d7(n):
    vsedel = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d % 10 == 7 and d != 7:
                vsedel.append(d)
            if (n // d) % 10 == 7 and (n // d) != 7:
                vsedel.append(n//d)

    return vsedel

k = 0
for i in range(600_000 + 1, 10 ** 10):
    a = d7(i)
    if len(a) > 0:
        print(i, min(a))
        k += 1
        if k == 5:
            break

print("****")

k = 0
for x in range(600_001, 10**10):
    d1 = 0
    for d in range(1, x + 1):
        if x % d == 0 and d % 10 == 7 and d != x and d != 7:
            d1 = d
            break
    if d1 != 0:
        print(x, d1)
        k += 1
        if k == 5:
            break
