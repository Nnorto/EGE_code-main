from math import dist
f = open('27_B_28766.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    s = s.split()
    x, y= float(s[0]), float(s[1])
    color, large = s[2][0], s[2][2:]
    zv = [x, y, color, large]
    data.append(zv)




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
def yelow_sverh_gigant(cluster):
    yg = []
    for x, y, color, large in cluster:
        if color == 'Z' and large == 'I':
            yg.append([x, y, color, large])
    return yg

yelow_sverh_gigant_for_clusters = [yelow_sverh_gigant(cluster) for cluster in clusters]
print(yelow_sverh_gigant_for_clusters[0])
print(yelow_sverh_gigant_for_clusters[1])
print(yelow_sverh_gigant_for_clusters[2])

def distans_yg(cluster):
    m = []
    for p0 in cluster:
        for p in cluster:
            if p != p0:
                m.append(dist(p[:2], p0[:2]))
    if m:
        return min(m)
    return 10**10

distans_yg_for_clusters = [distans_yg(cluster) for cluster in yelow_sverh_gigant_for_clusters]
b1 = int(min(distans_yg_for_clusters) * 10_000)
b2 = int(dist(centers[0][:2], centers[1][:2])* 10_000)
print(b1, b2)