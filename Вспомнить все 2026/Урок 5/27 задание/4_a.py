from math import dist


f = open('../file27/27_7_Zvar12A.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    p = [float(x) for x in s.split()]
    data.append(p)

print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 0.5]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster

anomaly = []
clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    if len(cluster) > 1:
        clusters.append(cluster)
    else:
        anomaly += cluster

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p0, p) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print(centers)
print('аномалии', anomaly)
X = [x for x, y in centers]
Y = [y for x, y in centers]
px = sum(X)/len(X)
py = sum(Y)/len(Y)
print(int(abs(px * 10_000)), int(abs(py * 10_000)))

from turtle import *
from random import *
c = 50
tracer(0)
screensize(10_000, 10_000)
up()

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(5, color)

for x, y in centers:
    goto(x * c, y * c)
    dot(10, 'black')

for x, y in anomaly:
    color = random(), random(), random()
    goto(x * c, y * c)
    dot(10, color)


hideturtle()
done()