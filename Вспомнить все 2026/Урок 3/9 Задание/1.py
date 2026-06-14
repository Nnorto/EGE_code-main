f = open('9.txt')
cnt = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if a[3] > a[0] + a[1] + a[2]:
        # if a[0] < a[1] < a[2] < a[3]:
        if len(set(a)) == 4:
            cnt += 1
print(cnt)