a = [int(x) for x in open('17_1.txt')]
max13 = max([x for x in a if x % 100 == 13])
count = 0
maxs = -1
for i in range(len(a)-2):
    if (len(str(a[i])) == 2) + (len(str(a[i + 1])) == 2) + (len(str(a[i + 2])) == 2) == 1:
        s = a[i] + a[i + 1] + a[i + 2]
        if s <= max13:
            count += 1
            maxs = max(maxs, s)
print(count, maxs)