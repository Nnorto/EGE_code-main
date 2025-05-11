f = open('9.txt')
ns = 0
for s in f:
    a = [int(x) for x in s.split()]
    ns += 1
    a.sort()
    b = [a.count(x) for x in a]
    if b.count(3) == 6 and b.count(1) == 1:
        pov = [x for x in a if a.count(x) == 3]
        np = [x for x in a if a.count(x) == 1][0]
        sr = sum(pov)/len(pov)
        if sr < np:
            print(ns)