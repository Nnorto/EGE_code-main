f = open('27 файлы/27-B1.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 11
si = maxs = knt = 0
prefs = [10**10] * k

for i in range(len(a)):
    si += a[i]
    if a[i] % 2 != 0:
        knt += 1
    if knt % 11 == 0:
        maxs = si
    else:
        if prefs[knt % k] != 10 ** 10:
            maybe_sum = si - prefs[knt % k]
            maxs = max(maxs, maybe_sum)

    prefs[knt % k] = min(prefs[knt % k], si)

print(maxs)