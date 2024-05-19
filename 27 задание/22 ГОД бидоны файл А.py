from math import *
f = open('27 файлы/27v03_A.txt')
n = int(f.readline())
a = [[int(x) for x in s.split()] for s in f]

""" ПОМЕНЯТЬ !!!"""
k = 20
""" ПОМЕНЯТЬ !!!"""


for i in range(len(a)):
    a[i][1] = ceil(a[i][1] / k)

mins = 10**30

for i in range(len(a)):
    tz = a[i][0]
    s = 0
    for j in range(len(a)):
        s += abs(tz - a[j][0]) * a[j][1]
    mins = min(mins, s)

print(mins)