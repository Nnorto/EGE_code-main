f = open('27a')
cl1, cl2 = [], []
for s in f:
    x, y = [float(x) for x in s.split()]
    if y < 5:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

from math import dist
def centr(cl):
    res = []
    for point1 in cl:
        sm = sum(dist(point1, point2) for point2 in cl)
        res.append((sm, point1))

    return min(res)[1]

centr1 = centr(cl1)
centr2 = centr(cl2)

px = (centr1[0] + centr2[0]) / 2
py = (centr1[1] + centr2[1]) / 2
print(abs(int(px * 10000)), abs(int(py * 10000)))