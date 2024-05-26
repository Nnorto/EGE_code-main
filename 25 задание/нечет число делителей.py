
for n in range(4_000_000, 12_000_000):
    vsedel = [1, n]
    if n ** 0.5 == int(n ** 0.5):
        for d in range(2, int(n ** 0.5)+1):
            if n % d == 0:
                if d * d == n:
                    vsedel.append(d)
                else:
                    vsedel.append(d)
                    vsedel.append(n//d)
    vsedel.sort()
    if len(vsedel) == 5:
        print(vsedel, n)


# имба способ через создание чисел
for i in range(int(4_000_000 ** 0.5), int(12_000_000 ** 0.5)+1):
    n = i ** 2
    a = [1, n]
    for d in range(2, i+1):
        if n % d == 0:
            if d == n//d:
                a.append(d)
            else:
                a.append(d)
                a.append(n // d)
    if len(a) == 5:
        print(a)