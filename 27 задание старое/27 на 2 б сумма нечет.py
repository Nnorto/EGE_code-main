f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
kch = 0
knch = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        kch += 1
    else:
        knch += 1

print(kch * knch)
