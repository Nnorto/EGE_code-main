f = open('../file27/27_10_Zvar15A.txt')

data = []

for s in f:
    s = s.replace(',', '.')
    p = [float(x) for x in s.split()]
    data.append(p)
print(len(data))


cluster1 = []
cluster2 = []
for age, pok in data:
    if age > 50 and pok < 13_500:
        cluster1.append([age, pok])
    elif age < 60 and pok > 10_000:
        cluster2.append([age, pok])

print(len(cluster1), len(cluster2))


pok1 = [y for x, y in cluster1]
pok2 = [y for x, y in cluster2]
srpok1 = sum(pok1)/len(pok1)
srpok2 = sum(pok2)/len(pok2)


clients1 = [[x, y] for x, y in cluster1 if abs(y - srpok1) <= 1000]
clients2 = [[x, y] for x, y in cluster2 if abs(y - srpok2) <= 1000]


C = srpok1 + srpok2
K = len(clients1) + len(clients2)
print(int(C*100), int(K*100))