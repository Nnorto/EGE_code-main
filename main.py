f = open('27 задание/27 файлы/27_A_2_day.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 100
s = 0
preflen = 0
pref = 0
maxl = 0
for i in range(len(a)):
    s += a[i]
    if s % 2 == 0 and s < 0:
        maxl = i + 1
    else:
        vs = s - pref
        vsl = i + 1 - preflen
        if vs < 0 and abs(vs) % 2 == 0:
            maxl = max(maxl, vs)
        if pref < s and abs(vs) % 2 == 0:
            pref = s
            preflen = i + 1

print(maxl)

f = open('27 задание/27 пример')
n = int(f.readline())
k = 2
a = [int(x) for x in f]
pref = [0] * k
prefd = [0] * k
s = maxd = 0

for i in range(n):
    s += a[i]
    if s < 0:
        if s % k == 0:
            maxd = i + 1
        else:
            vs = s - pref[s % k]
            vsd = i - prefd[s % k] + 1
            if vsd > maxd and vs % 2 == 0:
                maxd = vsd
            if pref[s % k] < s:
                pref[s % k] = s
                prefd[s % k] = i + 1

print(maxd)

f = open('27 задание/27 пример')
n = int(f.readline())
k = 2
a = [int(x) for x in f]
maxl = 0
st = 0
for i in range(len(a)):
    st += a[i]
    td = i + 1
    if st < 0 and st % 2 == 0:
        maxl = max(maxl, td)

print(maxl)
