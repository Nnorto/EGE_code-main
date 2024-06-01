from math import *

f = open('27 файлы/27B_2.txt')
n, m = map(int, f.readline().split())
k = 5
a = [0]
maxs = 0
for i in range(n):
    x = int(f.readline())
    a.append(ceil(x/k))

pref = [0] * len(a)
for i in range(1, len(a)):
    pref[i] = pref[i - 1] + a[i]

z1 = 0
maxs1 = 0
for i in range(len(a)):
    s = pref[min(i + m, len(a)-1)] - pref[max(i - m - 1, 0)]
    if s > maxs1:
        maxs1 = s
        z1 = i

for i in range(z1-m, z1+m+1):
    a[i] = 0

pref = [0] * len(a)
for i in range(1, len(a)):
    pref[i] = pref[i - 1] + a[i]

z2 = 0
maxs2 = 0
for i in range(len(a)):
    s = pref[min(i + m, len(a)-1)] - pref[max(i - m - 1, 0)]
    if s > maxs2:
        maxs2 = s
        z2 = i
print(maxs1+maxs2, z1, z2)