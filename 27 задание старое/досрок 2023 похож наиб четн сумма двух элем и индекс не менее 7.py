f = open('27 файлы/27-A.txt')
n = int(f.readline())
a = [int(x) for x in f]
maxs = maxch = maxnch = -10**10
k = 7

for i in range(k, len(a)):
    if a[i - k] % 2 == 0:
        maxch = max(maxch, a[i - k])
    else:
        maxnch = max(maxnch, a[i - k])

    if a[i] % 2 == 0:
        maxs = max(maxs, a[i] + maxch)
    else:
        maxs = max(maxs, a[i] + maxnch)

print(maxs)