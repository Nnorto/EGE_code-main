f = open('9.txt')
cnt = 0
for s in f:
    a = [int(x) for x in s.split()]
    p = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    if len(np) == 1 and len(p) == 6:
        if max(p) > np[0]:
            cnt += 1

print(cnt)
