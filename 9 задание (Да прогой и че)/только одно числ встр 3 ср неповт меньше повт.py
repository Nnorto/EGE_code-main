f = open('9.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    b = [a.count(x) for x in a]
    if b.count(3) == 3 and b.count(1) == 4:
        np = [x for x in a if a.count(x) == 1]
        p = [x for x in a if a.count(x) == 3]
        pnum = p[0]
        sr = sum(np)/len(np)
        if sr <= pnum:
            k += 1
print(k)