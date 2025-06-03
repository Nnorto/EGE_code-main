from math import dist
from random import random
from turtle import *

f = open('27B.txt')

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

anomaly = []
clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    if len(cluster) > 20:
        clusters.append(cluster)
    else:
        anomaly.append(cluster)

def dve_tochki(cluster):
    p1, p2 = 0, 0
    min_dist = 10**10
    for p0 in cluster:
        for p in cluster:
            if p != p0:
                if dist(p, p0) < min_dist:
                    min_dist = dist(p, p0)
                    p1, p2 = p, p0

    return [p1, p2]

sclad_sbor = [dve_tochki(cluster) for cluster in clusters]
print(sclad_sbor)
px = sum(p1[0] + p2[0] for p1, p2 in sclad_sbor) / (len(sclad_sbor)*2)
py = sum(p1[1] + p2[1] for p1, p2 in sclad_sbor) / (len(sclad_sbor)*2)

print(abs(int(px*10_000)), abs(int(py*10_000)))

tracer(0)
up()
c = 50
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(5, color)

for p in sclad_sbor:
    color = random(), random(), random()
    for x, y in p:
        goto(x * c, y * c)
        dot(10, color)

update()
done()


