f = open('27 пример')
N = int(f.readline())
a = list(map(int, f))
maxc = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        p = a[i] * a[j]
        if p % 14 == 0:
            maxc = max(maxc, p)
print(maxc)