from math import dist
f = open('27_A_31132.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    x, y, s = [x for x in s.split()]
    x = float(x)
    y = float(y)
    color = s[0]
    swet = s[1]
    razmer = s[2:]
    data.append([x, y, color, razmer])
print(data[0])

def red_gigatn(data):
    red = []
    for x, y, color, razmer in data:
        if color == 'M' and razmer == 'III':
            red.append([x, y, color, razmer])
    return red
red_gigants = red_gigatn(data)
print(len(red_gigants))

def get_cluster(p0):
    cluster = [p for p in data if dist(p[:2], p0[:2]) <= 1.5]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster

clusters = []
print(len(data))
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p0[:2], p[:2]) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print(centers)

dist_do_red = [p for p in red_gigants if dist(p[:2], centers[0][:2]) <= 1]
A1 = len(dist_do_red)
A2 = dist(centers[0][:2], centers[1][:2])
print(A1, int(A2*10_000))

from turtle import *
from random import *

c = 30
tracer(0)
up()
screensize(10000,10000)
for cluster in clusters:
    color = random(), random(), random()
    for x, y, cwet, razmer in cluster:
        goto(x * c, y * c)
        dot(5, color)
    write(f'{len(cluster)}')

for x, y, cwet, razmer in centers:
    goto(x * c, y * c)
    dot(10, 'black')


for x, y, cwet, razmer in red_gigants:
    goto(x * c, y * c)
    dot(10, 'red')

hideturtle()
done()

# 3 129201

