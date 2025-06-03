from math import dist
f = open('файлы/27_A_20911 (1).txt')
f.readline()
data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])
print(len(data), 'ALL')
def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) <= 2]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster
sm = 0
clusters = []
while len(data) != 0:
    cluster = get_cluster(data[0])
    print(len(cluster))
    sm += len(cluster)
    clusters.append(cluster)
print('proverka', sm)
def centr(cluster):
    m = []
    for p1 in cluster:
        summa = sum(dist(p1, p) for p in cluster)
        m.append([summa, p1])
    return min(m)[1]

centrs = [centr(cluster) for cluster in clusters]
Px = sum(x for x, y in centrs)/len(centrs)
Py = sum(y for x, y in centrs)/len(centrs)
print(abs(int(Px*10_000)), abs(int(Py*10_000)))

from turtle import *
from random import *
screensize(10000, 10000)
tracer(0)
up()

for cluster in clusters:
    color = random(), random(), random()
    for x,y in cluster:
        goto(x*15, y*15)
        dot(3, color)

goto(777, 777)
update()
done()