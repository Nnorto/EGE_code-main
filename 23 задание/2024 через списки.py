a = [0] * (30 + 1)
a[30] = 1
for i in range(29, 14-1, -1):
    if i + 2 <= 30:
        a[i] += a[i + 2]
    if i == 30 // 2:
        a[i] += a[i * 2]
    elif i * 2 <= 30 and i * 2 + 1 <= 30:
        a[i] += a[i * 2] + a[i * 2 + 1]
for i in range(13, 1 - 1, -1):
    if i + 2 <= 14:
        a[i] += a[i + 2]
    if i == 14 // 2:
        a[i] += a[i * 2]
    elif i * 2 <= 14 and i * 2 + 1 <= 14:
        a[i] += a[i * 2] + a[i * 2 + 1]
print(a[1])