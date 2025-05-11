f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k14 = k7 = k2 = k1 = 0

for i in range(len(a)):
    if a[i] % 14 == 0:
        k14 += 1
    elif a[i] % 7 == 0:
        k7 += 1
    elif a[i] % 2 == 0:
        k2 += 1
    else:
        k1 += 1

print(k14*(k7+k2+k1) + k7*k2 + k14*(k14 - 1) // 2)
