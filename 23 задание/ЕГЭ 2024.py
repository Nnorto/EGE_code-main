def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    else:
        return f(x - 2, y) + f(x // 2, y)

print(f(30, 14)*f(14, 1))


start = 30
fin = 1
a = [0]*(30+1)
a[start] = 1

for i in range(29, 13, -1):
    if i + 2 <= 30:
        a[i] += a[i + 2]
    if i * 2 <= 30:
        a[i] += a[i * 2]
    if i * 2 + 1 <= 30:
        a[i] += a[i * 2 + 1]

for i in range(13, 0, -1):
    if i + 2 <= 14:
        a[i] += a[i + 2]
    if i * 2 <= 14:
        a[i] += a[i * 2]
    if i * 2 + 1 <= 14:
        a[i] += a[i * 2 + 1]
print(a[1])