f = open('9.txt')

for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    p = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p) == 4 and len(np) == 3:
        if a[-1] in np:
            print(sum(a))
            break