from math import dist
from types import new_class

f = open('27_A_28766.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    x, y, s = s.split()
    x = float(x)
    y = float(y)
    color = s[0]
    svet = int(s[1])
    razm = s[2:]
    p = [x, y, color, razm]
    data.append(p)

print(len(data), data[0])


def red_gigant(data):
    red = []
    for x, y, color, razm in data:
        if color == 'Y' and razm == 'III':
            red.append([x, y, color, razm])
    return red

red_gigants = red_gigant(data)


def get_cluster(p0):
    cluster = [p for p in data if dist(p0[:2], p[:2]) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster


clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)


def center(cluster):
    m = []
    for p0 in cluster:
        sm = sum(dist(p[:2], p0[:2]) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]


centers = [center(cluster) for cluster in clusters]
print(centers)
print(len(red_gigants))

dist_do_red_gig = [dist(centers[1][:2], p[:2]) for p in red_gigants]
print(dist_do_red_gig)
A1 = min(dist_do_red_gig)
A2 = max(dist_do_red_gig)

print(int(A1*10_000), int(A2*10_000))

from turtle import *
from random import *
c = 30
tracer(0)
screensize(10_000, 10_000)
up()

for cluster in clusters:
    color = random(), random(), random()
    for x, y, cwet, razm in cluster:
        goto(x*c, y*c)
        dot(5, color)

for x, y, color, razm in centers:
    goto(x*c, y*c)
    dot(10, 'black')

for x, y, color, razm in red_gigants:
    goto(x * c, y * c)
    dot(10, 'red')

hideturtle()
done()