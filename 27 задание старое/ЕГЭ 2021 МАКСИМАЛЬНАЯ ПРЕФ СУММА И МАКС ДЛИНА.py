f = open('27 задание старое/27 файлы/27_A_префикс 263.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 100
s = 0
maxs, maxd = 0, 0
prefsnsm = 10**100
preflen = 0

for i in range(len(a)):
    s += a[i]
    if s % 2 == 0:
        dl = i + 1
        if maxs < s or (maxs == s and maxd < dl):
            maxs = s
            maxd = dl
    else:
        vs = s - prefsnsm
        maxd = max(maxd, i - prefsnsm + 1)

    if prefsnsm > s:
        prefsnsm = s
        preflen = i + 1
print(maxs, maxd)

# ИЛИ
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