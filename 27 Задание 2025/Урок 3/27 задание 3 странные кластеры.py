from math import *
from random import *
from turtle import *

f = open('27_103B.txt')

data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 1.5]
    if cluster:
        for p in cluster: data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
distributed = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    if len(cluster) > 1:
        clusters.append(cluster)
    else:
        distributed += cluster


print(distributed)
# not_distributed = distributed[0]
# def f(clusters):
#     min_dist = 10**10
#     min_cluster = 0
#     for cluster in clusters:
#         for p in cluster:
#             if dist(p, not_distributed) < min_dist:
#                 min_cluster = cluster
#                 min_dist = dist(p, not_distributed)
#
#     return min_cluster
# min_cluster = f(clusters)
# for cluster in clusters:
#     if cluster == min_cluster:
#         cluster.append(not_distributed)

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]

px = sum(x for x, y in centers) / len(centers)
py = sum(y for x, y in centers) / len(centers)

print(int(abs(px)*10_000), int(abs(py)*10_000))

tracer(0)
up()
screensize(10_000, 10_000)
c = 10

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x*c, y*c)
        dot(5, color)

for x, y in centers:
    color = random(), random(), random()
    goto(x*c, y*c)
    dot(15, color)
update()
done()