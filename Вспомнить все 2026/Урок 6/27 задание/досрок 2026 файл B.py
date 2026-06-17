from math import dist
from types import new_class

f = open('27_B_28766.txt')
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


def yellow_giant(data):
    yellow = []
    for x, y, color, razm in data:
        if color == 'Z' and razm == 'I':
            yellow.append([x, y, color, razm])
    return yellow

yellow_giants = yellow_giant(data)


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
print(len(yellow_giants))

def dist_for_yellow(yellow_giants):
    m = []
    for p0 in yellow_giants:
        d = [dist(p0[:2], p[:2]) for p in yellow_giants if p != p0]
        m.append(min(d))
    return min(m)

B1 = dist_for_yellow(yellow_giants)
print(B1)
B2 = dist(centers[0][:2], centers[1][:2])
print(B2)

print(int(B1*10_000), int(B2*10_000))

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
    write(f'{len(cluster)}')

for x, y, color, razm in centers:
    goto(x*c, y*c)
    dot(10, 'black')

for x, y, color, razm in yellow_giants:
    goto(x * c, y * c)
    dot(10, 'yellow')

hideturtle()
done()