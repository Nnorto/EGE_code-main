from math import dist
from turtle import *
from random import *
f = open('27_101B.txt')
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

def edge(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return max(m)[1]

edges = [edge(cluster) for cluster in clusters]

px = sum(x for x,y in edges) / len(edges)
py = sum(y for x,y in edges) / len(edges)

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
for x,y in edges:
    color = random(), random(), random()
    goto(x*c, y*c)
    dot(15, color)

goto(12796391, 123123123)
update()
done()