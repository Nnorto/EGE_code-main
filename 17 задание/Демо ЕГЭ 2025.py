f = open('demo_2025_17.txt')
a = []
for s in f:
    a.append(int(s))
min_el = min(a)
k = 0
maxs = -1
for i in range(len(a) - 1):
    if a[i] % 16 == min_el or a[i + 1] % 16 == min_el:
        k += 1
        maxs = max(maxs, a[i] + a[i + 1])

print(k, maxs)
f = open('17 задание/demo_2025_17.txt')
maxs = -1
a = [int(s) for s in f]
b = [x for x in a]
min_el = min(b)
count = 0
for i in range(len(a) - 1):
    if a[i] % 16 == min_el or a[i + 1] % 16 == min_el:
        count += 1
        maxs = max(maxs, a[i] + a[i + 1])
print(count, maxs, min_el)