f = open("Файлы/26-3.txt")
mesto, n = map(int, f.readline().split())
a = list(map(int, f))
a.sort()
count = 0
t_sum = 0
last = 0
for i in range(n):
    if t_sum + a[i] <= mesto:
        t_sum += a[i]
        count += 1
        last = a[i]
    else:
        break

max_el = mesto - t_sum + last
for x in reversed(range(len(a))):
    if max_el >= a[x]:
        max_el = a[x]
        break

print(count, max_el)