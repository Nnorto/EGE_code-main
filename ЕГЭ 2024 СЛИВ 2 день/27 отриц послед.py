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
    maxl = 0
    st = 0
    for i in range(len(a)):
        st += a[i]
        td = i + 1
        if st < 0 and st % 2 == 0:
            maxl = max(maxl, td)
    return maxl

from  random import *
n = 100
for i in range(100):
    a = [randrange(-100, 10) for x in range(n)]
    resA = A(a)
    resB = B(a)
    if resA != resB:
        print('wrong')
        print(a, resA, resB)
        break
