def vsedel(n):
    vd = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            vd.append(d)
            vd.append(n//d)
            if len(vd) > 6:
                return vd
        d += 1
    return vd


k = 0
count = 0
answ = []  # могу себе позволить лень переворачивать руками
for num in range(650_000+1, 659_999):
    alldel = vsedel(num)
    alldel.sort()
    if len(alldel) > 0:
        k = alldel[0] + alldel[-1]
        if len(alldel) == 6 and len(str(k)) == 4:
            answ.append([num, k])
            count += 1
        if count == 5:
            break

for x in reversed(answ):
    print(*x)  # зато ctrl+c ctrl +v :*
