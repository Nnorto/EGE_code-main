def vsedel(n):
    vd = [1, n]
    d = 2
    while d * d <= n:
        if n % d == 0:
            if d * d == n:
                vd.append(d)
            else:
                vd.append(d)
                vd.append(n // d)
        d += 1

    return vd

for num in range(10_271_400, 10272500+1):
    alldel = vsedel(num)
    if len(alldel) == 4:
        print(num)