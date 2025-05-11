f = open('27 файлы/27-B.txt')
n = int(f.readline())
a = [int(x) for x in f]
res = k14 = k7 = k2 = k1 = 0
k = 3

for i in range(k, len(a)):
    if a[i - k] % 14 == 0:
        k14 += 1
    elif a[i - k] % 7 == 0:
        k7 += 1
    elif a[i - k] % 2 == 0:
        k2 += 1
    else:
        k1 += 1

    if a[i] % 14 == 0:
        res += k14 + k7 + k2 + k1
    elif a[i] % 7 == 0:
        res += k14 + k2
    elif a[i] % 2 == 0:
        res += k14 + k7
    else:
        res += k14

print(res)

