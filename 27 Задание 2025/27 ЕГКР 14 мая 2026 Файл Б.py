from math import dist

f = open('файлы/27_B_29979.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    p = [float(x) for x in s.split()]
    data.append(p)

print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

print(len(data))

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print(centers)

ans1 = []
cnt = 0
for x,y in clusters[1]:
    xc, yc = centers[1]
    if abs(x - xc) <= 1 and abs(y - yc) <= 1:
        cnt += 1
        ans1.append([x, y])


ymax = centers[0][1]
ymin = centers[2][1]
d = abs(ymax - ymin)
print(cnt, int(d*10_000))
from turtle import *
from random import *
tracer(0)
up()
c = 50
screensize(10000, 10000)
for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*c, y*c)
        dot(5, color)

for x,y in centers:
    goto(x*c, y*c)
    dot(7, 'black')

for x,y in ans1:
    goto(x*c, y*c)
    dot(6, 'pink')

hideturtle()
done()