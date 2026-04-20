f = open('9.txt')
cnt = 0

for s in f:
    a = [int(x) for x in s.split()]
    if a[0] < a[1] < a[2] < a[3] < a[4]:
        if a[0] + a[4] <= a[1] + a[2] + a[3]:
            cnt += 1
            print(s)


print(cnt)

#138