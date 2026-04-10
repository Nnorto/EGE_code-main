from math import *
from random import *
from turtle import *
f = open('файлы/27_A_28766.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    s = s.split()
    color = s[2][0]
    razmer = s[2][2:]
    sveta = int(s[2][2])
    p = [float(s[0]), float(s[1]), color, razmer]
    data.append(p)

def get_cluster(p0):
    cluster = [p for p in data if dist(p[:2], p0[:2]) <= 1]
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
        summ = sum(dist(p0[:2], p[:2]) for p in cluster)
        m.append([summ, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]

def yelow_svgigant(cluster):
    gigant = []
    for p in cluster:
        if p[2] == 'Z' and p[3] == 'I':
            gigant.append(p)
    return gigant

def redgigant(cluster):
    gigant = []
    for p in cluster:
        if p[2] == 'Y' and p[3] == 'III':
            gigant.append(p)
    return gigant

def dist_gigant(gigant_cluster):
    m = []
    for p0 in gigant_cluster:
        for p in gigant_cluster:
            if p0 != p:
               m.append(dist(p[:2], p0[:2]))
    if m:
        return min(m)
    else:
        return 10**10


red_gigants = [redgigant(cluster) for cluster in clusters]
red_gigants = sum(red_gigants, [])

a = [dist(centers[1][:2], p[:2]) for p in red_gigants]
print(int(min(a)*10_000), int(max(a)*10_000))

# # 4940 74302

gigant_clusters = [yelow_svgigant(cluster) for cluster in clusters]
b_ans = [dist_gigant(gigant_cluster) for gigant_cluster in gigant_clusters]
# print(gigant_clusters[0])
# print(gigant_clusters[1])




# print('1 кластер:', len(gigant_clusters[0])) # max count GIGANT
# print('2 кластер:', len(gigant_clusters[1])) # min count GIGANT
# print('3 кластер:', len(gigant_clusters[2]))
# b1 = int(min(b_ans)*10_000)
# b2 = dist(centers[0][:2], centers[1][:2])
# print(b1, int(b2*10_000))
#
# # 1035 125591
tracer(0)
screensize(10_000, 10_000)
c = 100
up()

for cluster in clusters:
    color = random(), random(), random()
    for x, y, clr, rz in cluster:
        goto(x*c, y*c)
        dot(5, color)

color = 'red'
for x, y, clr, rz in red_gigants:
    goto(x*c, y*c)
    dot(7, color)

hideturtle()
done()