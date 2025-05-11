from math import *
f = open('27 задание старое/27 файлы/27B_3.txt')
n, k, m = map(int, f.readline().split())
a = [] # ПОМЕНЯТЬ!!!!
for i in range(n):
    x, y = map(int, f.readline().split())
    a.append([x, y])

dor = [0] * (a[-1][0] + 1)
for i in range(len(a)):
    dor[a[i][0]] = a[i][1]
# print('dor', dor)
pref = [0] * len(dor)
for i in range(1, len(dor)):
    pref[i] = pref[i-1] + dor[i]
# print('pref', pref)

maxs = 0
nl = 0
for i in range(len(pref)):
    if dor[i] != 0:
        s = pref[min(i+m, len(pref)-1)] - pref[max(i-m-1, 0)]
        if maxs < s:
            maxs = s
            nl = i
answ = 0
for i in range(len(a)):
    if abs(i - nl) <= m:
        answ += ceil(dor[i]/k)

print(answ)

