a = [0] * (30+1)
a[30] = 1
for i in range(30-1, 8-1, -1):
    if i + 1 <= 30:
        a[i] += a[i + 1]
    if i * 2 == 30:
        a[i] += a[i * 2]
    elif  i * 2 < 30:
        a[i] += a[i * 2] +  a[i * 2 + 1]
for i in range(8-1, 1-1, -1):
    if i + 1 <= 8:
        a[i] += a[i + 1]
    if i * 2 == 8:
        a[i] += a[i * 2]
    elif  i * 2 <= 8 and i * 2 + 1 <= 8:
        a[i] += a[i * 2] +  a[i * 2 + 1]
print(a)
