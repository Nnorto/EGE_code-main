f = open('27_104A.txt')

data = []
for s in f:
    s = s.replace(',', '.')
    data.append([float(x) for x in s.split()])
print(len(data))

clusters = []
distributed = []
cluster1 = []
cluster2 = []
for x,y in data:
    if x <= 53:
        cluster1.append([x,y])
    else:
        cluster2.append([x, y])


clusters.append(cluster1)
clusters.append(cluster2)
for cluster in clusters:
    print(len(cluster))

def sr_cost(cluster):
    sm = 0
    cnt = 0
    for p0 in cluster:
        sm += p0[1]
        cnt += 1
    return sm/cnt

def count_pok(cluster):
    y_cent = sr_cost(cluster)
    cnt = 0
    for x, y in cluster:
        if abs(y - y_cent) <= 1000:
            cnt += 1
    return cnt

costs = [sr_cost(cluster) for cluster in clusters]
print(costs)
counter = [count_pok(cluster) for cluster in clusters]
C = sum(costs)
K = sum(counter)
print(int(C*100), int(K*100))
