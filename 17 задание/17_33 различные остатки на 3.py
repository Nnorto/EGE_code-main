f = open('17_33.txt')
a = [int(s) for s in f]
count, maxs = 0, 0
ch = [x for x in a if x % 2 == 0]
sr = sum(ch)/len(ch)
for i in range(len(a) - 2):
    if (a[i] % 3) + (a[i + 1] % 3) + (a[i + 2]%3) == 3 and \
            a[i] % 3 != a[i + 1] % 3 != a[i + 2] % 3:
        if (a[i] > sr) + (a[i+1] > sr) + (a[i+2] > sr) == 1:
            s = a[i] + a[i+1] + a[i+2]
            count += 1
            maxs = max(maxs, s)


print(count, maxs)

ch = [x for x in a if x % 2 == 0]
sr = sum(ch)/len(ch)
maxs = -1
count = 0
for i in range(len(a) - 2):
    if ((a[i] % 3 + a[i+1] % 3 + a[i+2] % 3) == 3) and a[i] % 3 != a[i + 1] % 3:
        if (a[i] > sr) + (a[i+1] > sr) + (a[i+2] > sr) == 1:
            maxs = max(maxs, a[i] + a[i + 1] + a[i + 2])
            count += 1
print(count, maxs)
