f = open('9.txt')
cnt = 0
for s in f:
    a = [int(x) for x in s.split()]
    p = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p) == 4 and len(np) == 3:
        srall = sum(a) / len(a)
        srp = sum(p) / len(p)
        if srp > srall:
            cnt += 1
print(cnt)