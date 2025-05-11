f = open('9.txt')
ns = 0
for s in f:
    a = [int(x) for x in s.split()]
    ns += 1
    b = [a.count(x) for x in a]
    if a[0] <= a[1] <= a[2] <= a[3] <= a[4]:
        if b.count(1) < 5:
            p = [x for x in a if a.count(x) != 1]
            if sum(p) % 2 == 0:
                print(ns)
