f = open('27 файлы/27-A1.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 100
si = maxs = 0
prefs = [10**20] * k  # min sum ostat

for i in range(len(a)):
    si += a[i]
    osti = si % k
    if osti == 0:
        maxs = si
    else:
        maxs = max(maxs, si - prefs[osti])

    prefs[osti] = min(prefs[osti], si)

print(maxs)
