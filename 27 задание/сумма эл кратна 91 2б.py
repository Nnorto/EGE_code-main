f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 91
kost = [0] * k
res = 0
for i in a:
    ost = i % k
    res += kost[(91 - ost) % 91]
    kost[ost] += 1

print(res)