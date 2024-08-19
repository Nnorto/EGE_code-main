def f(x, y):
    if x == y:
        return 1
    if x > y or x == 15:
        return 0
    else:
        return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)


print(f(3, 9) * f(9, 25))

# или

a = [0] * 26
a[3] = 1

for i in range(4, 10):
    a[i] += a[i - 2]
    a[i] += a[i - 3]
    if i % 2 == 0:
        a[i] += a[i // 2]

for i in range(10, 26):
    if i != 15:
        if i - 2 >= 9:
            a[i] += a[i - 2]
        if i - 3 >= 9:
            a[i] += a[i - 3]
        if i % 2 == 0 and i // 2 >= 9:
            a[i] += a[i // 2]

print(a[25])