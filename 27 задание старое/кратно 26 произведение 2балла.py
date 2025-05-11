# Динамическое решение

f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k26 = k13 = k2 = k1 = 0
res = 0
for i in range(len(a)):
    if a[i] % 26 == 0:
        res += k26 + k1 + k2 + k13
        k26 += 1
    elif a[i] % 13 == 0:
        res += k26 + k2
        k13 += 1
    elif a[i] % 2 == 0:
        res += k26 + k13
        k2 += 1
    else:
        res += k26
        k1 += 1

print(res)

# Статика

f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k26 = k13 = k2 = k1 = 0
for i in range(len(a)):
    if a[i] % 26 == 0:
        k26 += 1
    elif a[i] % 13 == 0:
        k13 += 1
    elif a[i] % 2 == 0:
        k2 += 1
    else:
        k1 += 1


print(k26 * (k1 + k2 + k13) + k13 * k2 + (k26 - 1) * k26 // 2)

