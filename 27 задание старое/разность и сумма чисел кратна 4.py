f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 4
ost0 = [0] * k
ost1 = [0] * k
ost2 = [0] * k
ost3 = [0] * k
res = 0
for i in range(len(a)):
    ost = a[i] % k
    ostnap = (k - ost) % k
    if i % 4 == 0:
        res += ost0[ostnap]
        ost0[ost] += 1
    elif i % 4 == 1:
        res += ost1[ostnap]
        ost1[ost] += 1
    elif i % 4 == 2:
        res += ost2[ostnap]
        ost2[ost] += 1
    else:
        res += ost3[ostnap]
        ost3[ost] += 1

print(res)