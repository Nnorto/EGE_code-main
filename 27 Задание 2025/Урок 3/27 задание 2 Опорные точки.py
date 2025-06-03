from math import dist
from turtle import *
from random import *
f = open('27_102B.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])

print(f'{len(data)=}')

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster
clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def oporno(cluster):
    maxx = -10**10
    maxy = -10**10
    minx = 10**10
    miny = 10**10
    verx, niz, levo, pravo = 0, 0, 0, 0
    for p in cluster:
        x, y = p
        if minx > x:
            levo = p
            minx = x
        if maxx < x:
            pravo = p
            maxx = x
        if miny > y:
            niz = p
            miny = y
        if maxy < y:
            verx = p
            maxy = y
    return [verx, niz, levo, pravo]

tochki = [oporno(cluster) for cluster in clusters]

# smx = smy = 0
# cx = cy = 0
# for cluster in tochki:
#     for x, y in cluster:
#         smx += x
#         smy += y
#         cx += 1
#         cy += 1
# srx = smx/cx
# sry = smy/cy
# print(abs(int(srx*10_000)), abs(int(sry*10_000)))

px = sum(p1[0] + p2[0] + p3[0] + p4[0] for p1, p2, p3, p4 in tochki) / (len(tochki)*4)
py = sum(p1[1] + p2[1] + p3[1] + p4[1] for p1, p2, p3, p4 in tochki) / (len(tochki)*4)
print(abs(int(px*10_000)), abs(int(py*10_000)))

tracer(0)
up()
c = 30
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*c, y*c)
        dot(5, color)

for p in tochki:
    color = random(), random(), random()
    for x,y in p:
        goto(x*c, y*c)
        dot(15, color)

goto(12796391, 123123123)
update()
done()

