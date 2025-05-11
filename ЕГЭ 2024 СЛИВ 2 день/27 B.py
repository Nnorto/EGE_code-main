f = open('27 задание старое/27 файлы/27_A_префикс 263.txt')
n = int(f.readline())
k = 2
a = [int(x) for x in f]
pref = [10 ** 100] * k
prefd = [10 ** 100] * k
s = maxs = maxd = 0
for i in range(n):
    s += a[i]
    if s % k == 0:
        maxs = s
        maxd = i + 1
    else:
        vs = s - pref[s % k]
        vsd = i - prefd[s % k] + 1
        if vs > maxs or (vs == maxs and vsd > maxd):
            maxs = vs
            maxd = vsd
    if pref[s % k] > s:
        pref[s % k] = s
        prefd[s % k] = i + 1

print(maxs, maxd)