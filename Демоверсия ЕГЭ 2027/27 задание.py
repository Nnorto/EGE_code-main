from csv import unix_dialect


def cinetic(p):
    vx, vy, m = p[2:5]
    return m*(vx**2 + vy**2)/2
R = 0.5
f = open('demo_27.txt')
data = []
for s in f:
    x, y, vx, vy, m, priznak = s.split()
    p = [float(x), float(y), float(vx), float(vy), float(m), priznak]
    p.append(cinetic(p))
    data.append(p)

def get_cluster(p0):
    cluster = [p for p in data if abs(cinetic(p) - cinetic(p0)) <= R]
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
        sm = sum(abs(p[-1] - p0[-1]) for p in cluster)
        m.append([sm, p0])
    return min(m)[1]


centers = [center(cluster) for cluster in clusters]
for p in centers: print(p)
from math import dist

def dist_point(cluster):
    m = []
    for p0 in cluster:
        if p0[-2] == 'II':
            for p in cluster:
                if p[-2] == 'II':
                    m.append(dist(p[:2], p0[:2]))
    return max(m)

dist_points = [dist_point(cluster) for cluster in clusters]

Q1 = max(dist_points)
print(int(Q1*10_000))

center_cinetic = [p[-1] for p in centers]


Q2 = max(center_cinetic)
print(int(Q2*10_000))