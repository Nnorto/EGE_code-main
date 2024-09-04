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
