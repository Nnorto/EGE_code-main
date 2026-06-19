from math import dist
f = open('27_B_31132.txt')
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

def goluboi(data):
    gay = []
    for x, y, color, razmer in data:
        if color == 'O' and razmer == 'III':
            gay.append([x, y, color, razmer])
    return gay
goluboi_gigants = goluboi(data)
print('голубой', len(goluboi_gigants))

def yellow_karl(data):
    yellow = []
    for x, y, color, razmer in data:
        if color == 'G' and razmer == 'V':
            yellow.append([x, y, color, razmer])
    return yellow
yellow_gigants = yellow_karl(data)
print('жёлтый', len(yellow_gigants))

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

dist_do_gay = [dist(p0[:2], p[:2]) for p0 in centers for p in goluboi_gigants]
B1 = min(dist_do_gay)
yellow_gigants_cluster1 = [[x, y, color, razmer] for x, y, color, razmer in clusters[0] if color == 'G' and razmer == 'V']
yellow_gigants_cluster2 = [[x, y, color, razmer] for x, y, color, razmer in clusters[1] if color == 'G' and razmer == 'V']
yellow_gigants_cluster3 = [[x, y, color, razmer] for x, y, color, razmer in clusters[2] if color == 'G' and razmer == 'V']
B2 = len(yellow_gigants_cluster1)
print(int(B1*10_000), B2)

# 4601 13


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

for x, y, cwet, razmer in goluboi_gigants:
    goto(x * c, y * c)
    dot(10, 'blue')

for x, y, cwet, razmer in yellow_gigants:
    goto(x * c, y * c)
    dot(10, 'yellow')

hideturtle()
done()

