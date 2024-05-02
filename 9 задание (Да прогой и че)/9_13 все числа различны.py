f = open('файлы/9_13')
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    if (a[-1] > a[0] + a[1] + a[2]) and (len(a) == len(set(a))):
        count += 1
print(count)