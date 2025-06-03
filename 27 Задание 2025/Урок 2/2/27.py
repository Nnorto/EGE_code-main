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


clusters = []
anomaly_clients = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    if len(cluster) > 1:
        clusters.append(cluster)
    else:
        anomaly_clients += cluster


def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]


def client(cent):
    clients = anomaly_clients
    max_dist = 0
    max_client = 0
    for p in clients:
        if dist(p, cent) > max_dist:
            max_client = p
            max_dist = dist(p, cent)
    return max_client


centers = [center(cluster) for cluster in clusters]
clients = [client(cent) for cent in centers]
px = sum(x for x, y in clients) / len(clients)
py = sum(y for x, y in clients) / len(clients)
print(abs(int(px * 10_000)), abs(int(py * 10_000)))

tracer(0)
up()
screensize(10_000, 10_000)
c = 30

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(5, color)

for x, y in anomaly_clients:
    color = random(), random(), random()
    goto(x * c, y * c)
    dot(10, color)

for i in range(len(centers)):
    color = random(), random(), random()
    x1, y1 = centers[i]
    x2, y2 = clients[i]
    goto(x1 * c, y1 * c)
    dot(15, color)
    down()
    goto(x2 * c, y2 * c)
    dot(15, color)
    up()
update()
done()
