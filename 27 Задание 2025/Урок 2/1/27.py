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
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p, p0) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

def client(cluster):
    cent = center(cluster)
    max_client = 0
    max_dist = 0
    for p in cluster:
        if dist(p, cent) > max_dist:
            max_dist = dist(p, cent)
            max_client = p
    return max_client

clients = [client(cluster) for cluster in clusters]
centers = [center(cluster) for cluster in clusters]

px = sum(x for x, y in clients) / len(clients)
py = sum(y for x, y in clients) / len(clients)

print(abs(int(px*10_000)), abs(int(py*10_000)))

tracer(0)
up()
c = 52
screensize(10_000, 10_000)

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * c, y * c)
        dot(5, color)

for i in range(len(centers)):
    client_x, client_y = clients[i]
    center_x, center_y = centers[i]
    color = random(), random(), random()
    goto(client_x * c, client_y * c)
    dot(15, color)
    down()
    goto(center_x * c, center_y * c)
    dot(20, color)
    up()
update()
done()