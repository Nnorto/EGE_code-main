f = open('9.txt')
res = []
for s in f:
    a = [int(x) for x in s.split()]
    b = [a.count(x) for x in a]
    if b.count(3) == 3 and b.count(1) == 3:
        p = [x for x in a if a.count(x) > 1]
        np = [x for x in a if a.count(x) == 1]
        if p[0] < min(np):
            res += a

print(sum(res)/len(res))


f = open('9.txt')
sm = 0
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    b = [a.count(x) for x in a]
    if b.count(3) == 3 and b.count(1) == 3:
        p = [x for x in a if a.count(x) > 1]
        np = [x for x in a if a.count(x) == 1]
        if p[0] < min(np):
            sm += sum(a)
            k += 1
print(sm/(k*6))