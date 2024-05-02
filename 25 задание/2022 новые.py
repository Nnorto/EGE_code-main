from math import ceil, sqrt


def m(n):
    count = []
    p = 1
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            count.append(i)
    if len(count) >= 5:
        for i in range(5):
            p *= count[i]
        return p
    else:
        return 0


for x in range(200000001, 300000000):
    if 0 < m(x) < x:
        print(m(x))
