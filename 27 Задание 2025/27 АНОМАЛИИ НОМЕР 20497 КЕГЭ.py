from math import *

f = open('файлы/27.19.B_20497.txt')

data = []
for s in f:
    data.append([float(x) for x in s.split()])

print(len(data))

def get_clusters(p0):
    cluster = [p for p in data if dist(p, p0) < 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_clusters(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
while data:
    cluster = get_clusters(data[0])
    if len(cluster) > 10:
        print(len(cluster))
        clusters.append(cluster)

from turtle import *
from random import *
tracer(0)
up()
screensize(10000, 10000)
for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x*5, y*5)
        dot(3, color)
goto(500, 500)
update()
exitonclick()
def edge(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return max(m)[1]

edges = [edge(cluster) for cluster in clusters]
tx = sum(x for x, y in edges) / len(edges)
ty = sum(y for x, y in edges) / len(edges)
print(int(tx*10000), int(ty*10000))

# 13258 2656 a
#-209434 474989
