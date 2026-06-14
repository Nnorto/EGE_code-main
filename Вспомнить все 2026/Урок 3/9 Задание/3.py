f = open('9.txt')
pn = 0
for s in f:
    a = [int(x) for x in s.split()]
    pn += 1
    a.sort()
    if a[3] < a[0] + a[1] + a[2]:
       if a[0] + a[3] != a[1] + a[2]:
           print(pn, a)