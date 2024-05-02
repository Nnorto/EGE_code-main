f = open('файлы/9_10')
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    if (a[0] + a[-1])**2 > (a[1] ** 2 + a[2] ** 2 + a[3] ** 2):
        count += 1
print(count)