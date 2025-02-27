f = open('27b')
cl1, cl2, cl3 = [], [], []
for s in f:
    x, y = [float(x) for x in s.split()]
    if x < 0:
        cl1.append((x, y))
    elif y < 8:
        cl2.append((x, y))
    else:
        cl3.append((x, y))
from math import dist
def centr(cl):
    res = []
    for point1 in cl:
        sm = sum(dist(point1, point2) for point2 in cl)
        res.append((sm, point1))

    return min(res)[1]

centr1 = centr(cl1)
centr2 = centr(cl2)
centr3 = centr(cl3)

px = (centr1[0] + centr2[0] + centr3[0]) / 3
py = (centr1[1] + centr2[1] + centr3[1]) / 3
print(abs(int(px * 10000)), abs(int(py * 10000)))