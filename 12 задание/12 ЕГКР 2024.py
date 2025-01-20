maxs = -1
for n in range(4, 10_000):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        if '333' in s:
            s = s.replace('333', '5', 1)
    summa = sum(map(int, s))
    if summa > maxs:
        maxs = summa

print(maxs)