a = list(map(int, open("17 файлы/17файл.txt")))
ch = [x for x in a if x % 2 != 0]
sr = sum(ch)/len(ch)
maxs = -1
count = 0
for i in range(len(a) - 2):
    if ((a[i] % 3 + a[i+1] % 3 + a[i+2] % 3) == 3) and a[i] % 3 != a[i + 1] % 3:
        if (a[i] < sr) + (a[i+1] < sr) + (a[i+2] < sr) == 1:
            maxs = max(maxs, a[i] + a[i + 1] + a[i + 2])
            count += 1
print(count, maxs)