f = open('9.txt')
ns = 0
sm = 0
for s in f:
    a = [int(x) for x in s.split()]
    ns += 1
    a.sort()
    b = [a.count(x) for x in a]
    # if b.count(1) == 4:
    if len(a) == len(set(a)):
        ks = (a[0] + a[3])**2
        kyb = a[1]**3 + a[2]**3
        if ks > kyb:
            sm += ns
print(sm)
