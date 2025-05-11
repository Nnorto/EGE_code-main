from math import *
f = open('27 файлы/27v05_A.txt')
n, m = map(int, f.readline().split())
a = []
k = 15  # ПОМЕНЯТЬ!!!!
for i in range(n):
    x, y = map(int, f.readline().split())
    a.append([x, ceil(y/k)])

maxs = 0
for i in range(len(a)):
    s = 0
    tf = a[i][0]  # текущая ферма
    for j in range(len(a)):
        if abs(a[j][0] - tf) <= m:
            s += a[j][1]
    maxs = max(maxs, s)

print(maxs)