from math import dist
f = open('27_A_28766.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    s = s.split()
    x, y= float(s[0]), float(s[1])
    color, large = s[2][0], s[2][2:]
    zv = [x, y, color, large]
    data.append(zv)

red_gigant = []
for x, y, color, large in data:
    if color == 'Y' and large == 'III':
            red_gigant.append([x, y, color, large])


def get_cluster(p0):
    cluster = [p for p in data if dist(p[:2], p0[:2]) <= 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        new_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(new_clusters, [])
    return cluster
print(len(data))
clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def center(cluster):
    m = []
    for p0 in cluster:
        smm = sum(dist(p[:2], p0[:2]) for p in cluster)
        m.append([smm, p0])
    return min(m)[1]

centers = [center(cluster) for cluster in clusters]
print(centers)
dist_for_red_gigant = [dist(centers[1][:2], p[:2]) for p in red_gigant]
a1 = int(min(dist_for_red_gigant)*10_000)
a2 = int(max(dist_for_red_gigant)*10_000)
print(a1, a2)