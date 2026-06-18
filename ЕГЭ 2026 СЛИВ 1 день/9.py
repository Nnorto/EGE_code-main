f = open('9.txt')
cnt = 0
for s in f:
    a = [int(x) for x in s.split()]
    p3 = [x for x in a if a.count(x) == 3]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    if len(p3) == 3 and len(p2) == 2 and len(np) == 2:
        mpov = max(p3+p2)
        if mpov < max(np):
            cnt += 1
print(cnt)