from math import dist

f = open('файлы/27_B_23209.txt')
f.readline()
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
    print('кл-во звезд:', len(cluster))
    if len(cluster) > 1:
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
X = [centers[0][0], centers[2][0]]
Y = [centers[0][1], centers[2][1]]
print(X, Y)
qx = X[0] - X[1]
qy = Y[0] - Y[1]
print(int(abs(qx*10_000)), int(abs(qy*10_000)))
from turtle import *
from random import *

tracer(0)
up()
c = 10
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*c, y*c)
        dot(10, color)
hideturtle()
done()