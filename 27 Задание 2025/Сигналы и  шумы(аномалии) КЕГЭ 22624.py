from math import dist

f = open('файлы/27B_22624.txt')

data = []
for s in f:
    data.append([float(x) for x in s.split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
anomaly = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    if len(cluster) > 5:
        clusters.append(cluster)
    else:
        anomaly.append(cluster)
def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
px = sum(x for x, y in centers)/len(centers)
py = sum(y for x, y in centers)/len(centers)

print(int(abs(px)*10000), int(abs(py)*10000))

from turtle import *
from random import *

up()
tracer(0)
c = 10
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*c, y*c)
        dot(5, color)

for x,y in centers:
    color = random(), random(), random()
    goto(x*c, y*c)
    dot(15, color)

for cluster in anomaly:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(10, color)
update()
done()