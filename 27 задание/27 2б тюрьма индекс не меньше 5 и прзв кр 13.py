f = open('27 файлы/27-B.txt')
n = int(f.readline())
k = 5
a = [int(x) for x in f]
res = k13 = k1 = 0
for i in range(k, len(a)):
    if a[i - k] % 13 == 0:
        k13 += 1
    else:
        k1 += 1
    if a[i] % 13 == 0:
        res += k13 + k1
    else:
        res += k13

print(res)


