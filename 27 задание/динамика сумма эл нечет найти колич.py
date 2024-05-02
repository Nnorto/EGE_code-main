f = open('27 файлы/27_B.txt')
n = int(f.readline())
kch = knch = res = 0
a = list(map(int, f))

for i in range(len(a)):
    if a[i] % 2 == 0:
        res += knch
        kch += 1
    else:
        res += kch
        knch += 1

print(res)