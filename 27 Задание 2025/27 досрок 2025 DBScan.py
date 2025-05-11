from turtle import *
from random import *
from math import *

f = open('файлы/27_B_21425.txt')
data = []
for s in f:
    data.append([float(x) for x in s.split()])
print(len(data))
def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 5]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster
summa = 0
clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    summa += len(cluster)
    clusters.append(cluster)
print(f'{summa=}')
tracer(0)
up()
screensize(10000, 10000)
for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x*10, y*10)
        dot(3, color)

def cent(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

cents = [cent(cluster) for cluster in clusters]
Px = sum([x for x, y in cents]) / len(cents)
Py = sum([y for x, y in cents]) / len(cents)
print(int(Px*10000), int(Py*10000))
goto(777, 777)
update()
done()

# 167990 73043
# 122627 29105