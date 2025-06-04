
from math import dist
from random import random
from turtle import *

f = open('27_105B.txt')

data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])


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

def plotnya_tochka(cluster):
    m = []
    for p0 in cluster:
        clients = [p for p in cluster if dist(p, p0) <= 1]
        m.append([len(clients), p0])
    m.sort()
    return [m[-1][1], m[-2][1]]
tochki = [plotnya_tochka(cluster) for cluster in clusters]
px = sum(t1[0] + t2[0] for t1, t2 in tochki) / (len(tochki)*2)
py = sum(t1[1] + t2[1] for t1, t2 in tochki) / (len(tochki)*2)
print(abs(int(px * 10_000)), abs(int(py * 10_000)))

tracer(0)
c = 30
up()
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*c, y*c)
        dot(5, color)
for cluster in tochki:
    for x,y in cluster:
        color = random(), random(), random()
        goto(x*c, y*c)
        dot(15, color)


update()
done()