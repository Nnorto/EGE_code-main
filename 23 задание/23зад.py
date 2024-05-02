a = [0]*15
a[2] = 1

for i in range(3, 7):
    a[i] += a[i - 1]
    a[i] += a[i - 3]
    if i % 2 == 0:
        a[i] += a[i // 2]

for i in range(7, 11):
    if i - 1 >= 6:
        a[i] += a[i - 1]
    if i - 3 >= 6:
        a[i] += a[i - 3]
    if i // 2 >= 6 and i % 2 == 0:
        a[i] += a[i // 2]

for i in range(11, 15):
    if i - 1 >= 10:
        a[i] += a[i - 1]
    if i - 3 >= 10:
        a[i] += a[i - 3]
    if i // 2 >= 10 and i % 2 == 0:
        a[i] += a[i // 2]

print(a)