f = open('9')
c = 0
for z in f:
    a = list(map(int, z.split()))
    a.sort()
    if a[-1] < sum(a) - max(a):
        if max(a) + min(a) == a[1] + a[2]:
            c += 1
print(c)


