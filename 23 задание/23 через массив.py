a = [0] * 24
a[23] = 1
for i in range(22, 1, -1):
    if i + 2 <= 23:
        a[i] += a[i + 2]
    if i + 5 <= 23:
        a[i] += a[i + 5]

print(a)