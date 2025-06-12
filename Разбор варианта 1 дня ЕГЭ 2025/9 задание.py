f = open('9.txt')
ns = 0
for s in f:
    ns += 1
    a = [int(x) for x in s.split()]
    b = [a.count(x) for x in a]
    if b.count(3) == 3 and b.count(1) == 3:
        p = [x for x in a if a.count(x) > 1]
        np = [x for x in a if a.count(x) == 1]
        if p[0] > (sum(np)/len(np)):
            print(ns)
