from math import dist
from random import random
from turtle import *

f = open('27A.txt')

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
    return max(m)[1]

tochki = [plotnya_tochka(cluster) for cluster in clusters]
px = sum(x for x, y in tochki) / len(tochki)
py = sum(y for x, y in tochki) / len(tochki)
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
for x,y in tochki:
    color = random(), random(), random()
    goto(x*c, y*c)
    dot(15, color)


update()
done()