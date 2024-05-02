f = open('27 файлы/27-B1.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 100
si, res = 0, 0
pref_c = [0]*k

for i in range(len(a)):
    si += a[i]
    osti = si % k
    if osti == 0:
        res += 1
    res += pref_c[osti]
    pref_c[osti] += 1

print(res)