from math import dist

f = open('файлы/27.19.A_20497.txt')
data = []
for s in f:
    p = [float(x) for x in s.split()]
    data.append(p)
print(len(data))


def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 0.4]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
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


def edge(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return max(m)[1]


edges = [edge(cluster) for cluster in clusters]
print(edges)
X = [x for x, y in edges]
Y = [y for x, y in edges]
tx = sum(X) / len(X)
ty = sum(Y) / len(Y)
print(int(abs(tx * 10_000)), int(abs(ty * 10_000)))

from turtle import *
from random import *


tracer(0)
up()
c = 50
screensize(10_000, 10_000)
for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(3, color)

for cluster in anomaly:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(7, color)

# рисуем края
for x, y in edges:
    goto(x * c, y * c)
    dot(7, 'black')

hideturtle()
done()