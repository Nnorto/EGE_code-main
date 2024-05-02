f = open('27 пример')
N = int(f.readline())
a = list(map(int,f))
d = 160
p = 7
res1 = 0
res2 = 0
maxc = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] % d != a[j] % d:
            if a[i] % p == 0 or a[j] % p == 0:
                if a[i] + a[j] > maxc:
                    maxc = a[i] + a[j]
                    res1 = a[i]
                    res2 = a[j]

print(res1, res2)