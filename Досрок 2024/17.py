f = open("17.txt")
a = list(map(int,f))
el19 = [x for x in a if x % 19 == 0]
max19 = max(el19)
count = 0
maxs = -1000
for i in range(len(a) - 1):
    if (a[i] > max19) + (a[i+1] > max19) >= 1:
        count += 1
        maxs = max(maxs,a[i] + a[i+1])
print(count, maxs)