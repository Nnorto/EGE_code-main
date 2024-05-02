f = open("Файлы/26-3.txt")
mesto, n = map(int, f.readline().split())
a = list(map(int, f))
a.sort()
ts = 0
count = 0
for i in range(n):
    if ts + a[i] <= mesto:
        ts += a[i]
        count += 1
    else:
        break
ts = ts - a[count - 1]
last = 0
for i in range(count, n):
    if ts + a[i] <= mesto:
        last = a[i]
    else:
        break
print(count, last)