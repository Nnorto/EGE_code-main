f = open('9.txt')
cnt = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if a[3] < a[0] + a[1] + a[2]:
        # b = [a.count(x) for x in a]
        # if b.count(2) == 2:
        if len(set(a)) == 3:
            cnt += 1
print(cnt)