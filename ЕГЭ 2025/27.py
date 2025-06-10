from math import *

f = open('файлы/27_B_21932.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])

def get_clusters(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_clusters(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
while len(data) != 0:
    cluster = get_clusters(data[0])
    print(len(cluster))
    if len(cluster) > 1:
        clusters.append(cluster)

def centr(cluster):
    m = []
    for p0 in cluster:
        summ = sum(dist(p, p0) for p in cluster)
        m.append([summ, p0])
    return min(m)[1]

minc = min(clusters, key=len)
maxc = max(clusters, key=len)
Px = centr(minc)[0]
Py = centr(maxc)[1]
print(int(Px*10000) + int(Py*10000))


centers = []
sr = sum(x + y for x, y in centers)/(len(centers) * 2)
