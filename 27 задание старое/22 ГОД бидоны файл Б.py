from math import *
f = open('27 файлы/27v03_B.txt')
n = int(f.readline())
a = [[int(x) for x in s.split()] for s in f]

""" ПОМЕНЯТЬ !!!"""
k = 20
""" ПОМЕНЯТЬ !!!"""


for i in range(len(a)):
    a[i][1] = ceil(a[i][1] / k)

s = 0
for i in range(len(a)):
    s += a[i][1] * (a[i][0] - a[0][0])
mins = s

fs = 0
for x in range(1, len(a)):
    fs += a[x][1]
bs = a[0][1]

for i in range(1, len(a)):
    ots = a[i][0] - a[i - 1][0]
    s += -(fs * ots) + (bs * ots)
    fs -= a[i][1]
    bs += a[i][1]
    mins = min(mins, s)

print(mins)