f = open('../file27/27_10_Zvar15B.txt')

data = []

for s in f:
    s = s.replace(',', '.')
    p = [float(x) for x in s.split()]
    data.append(p)
print(len(data))

cluster1 = []
cluster2 = []
cluster3 = []
for age, pok in data:
    if age < 40:
        cluster1.append([age, pok])
    elif 40 < age < 80:
        cluster2.append([age, pok])
    else:
        cluster3.append([age, pok])
print(len(cluster1), len(cluster2), len(cluster3))

pok1 = [y for x, y in cluster1]
pok2 = [y for x, y in cluster2]
pok3 = [y for x, y in cluster3]
srpok1 = sum(pok1) / len(pok1)
srpok2 = sum(pok2) / len(pok2)
srpok3 = sum(pok3) / len(pok3)

clients1 = [[x, y] for x, y in cluster1 if abs(y - srpok1) <= 1000]
clients2 = [[x, y] for x, y in cluster2 if abs(y - srpok2) <= 1000]
clients3 = [[x, y] for x, y in cluster3 if abs(y - srpok3) <= 1000]

C = srpok1 + srpok2 + srpok3
K = len(clients1) + len(clients2) + len(clients3)
print(int(C * 100), int(K * 100))
# 2878142 185600
