
f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 24
kost = [0]*k
for i in range(len(a)):
    kost[a[i] % k] += 1
itog = kost[0] * (kost[0] - 1) // 2 + kost[12] * (kost[12] - 1) // 2
for i in range(1, k//2):
    itog += kost[i] * kost[k - i]
print(itog)






