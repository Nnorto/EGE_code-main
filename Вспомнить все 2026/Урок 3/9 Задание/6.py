f = open('9.txt')
pn = 0
for s in f:
    a = [int(x) for x in s.split()]
    pn += 1
    p = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p) == 2 and len(np) == 4:
        srnp = sum(np)/len(np)
        if p[0] > srnp:
            print(pn, a)
