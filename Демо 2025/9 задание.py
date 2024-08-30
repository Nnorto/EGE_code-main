f = open('9 файл')
c = 0
for s in f:
    # a = [int(x) for x in s.split()]
    a = list(map(int, s.split()))
    b = [a.count(x) for x in a]
    if b.count(3) == 3 and b.count(1) == 3:
        sump = 0
        for i in range(len(a)):
            if b[i] == 3:
                sump += a[i]
        sumnp = 0
        for i in range(len(a)):
            if b[i] == 1:
                sumnp += a[i]
        if sump ** 2 > sumnp ** 2:
            c += 1

print(c)