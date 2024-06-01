from math import *

f = open('27 файлы/27A_2.txt')
n, m = map(int, f.readline().split())
k = 5
a = []
maxs = 0
for i in range(n):
    x = int(f.readline())
    a.append(ceil(x/k))

for i in range(len(a)):
    for j in range(i + k, len(a)):
        s = 0
        for z in range(len(a)):
            if abs(i - z) <= m:
                s += a[z]
            elif abs(j - z) <= m:
                s += a[z]
        maxs = max(maxs, s)

print(maxs)
