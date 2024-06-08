def B(m):
    a = m
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
    return maxl

def A(m):
    k = 2
    a = m
    pref = [10 ** 100] * k
    prefd = [10 ** 100] * k
    s = maxs = maxd = 0
    for i in range(n):
        s += a[i]
        if s < 0:
            if s % k == 0:
                maxs = s
                maxd = i + 1
            else:
                vs = s - pref[s % k]
                vsd = i - prefd[s % k] + 1
                if vsd > maxd and vs < 0:
                    maxs = vs
                    maxd = vsd
            if pref[s % k] > s:
                pref[s % k] = s
                prefd[s % k] = i + 1

    return maxd
from  random import *
n = 100
for i in range(100):
    a = [randrange(-100, 1) for x in range(n)]
    resA = A(a)
    resB = B(a)
    if resA != resB:
        print('wrong')
        print(a, resA, resB)
        break