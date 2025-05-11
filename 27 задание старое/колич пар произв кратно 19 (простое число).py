f = open('27 файлы/27_A.txt')
n = int(f.readline())
a = [int(x) for x in f]
k19 = 0
k1 = 0

for i in range(len(a)):
    if a[i] % 19 == 0:
        k19 += 1
    else:
        k1 += 1

print(k19 * k1 + ((k19-1) * k19)//2)
