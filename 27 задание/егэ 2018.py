f = open('27 пример')
N = int(f.readline())
a = list(map(int,f))
k = 5
c = 0
for i in range(len(a)):
    for j in range(i + k, len(a)):
        p = a[i] * a[j]
        if p % 13 == 0:
            c += 1
print(c)