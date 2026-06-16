f = open('../file17/17_23.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if x % 32 == 0]
k = len(b)
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if (x < 0) + (y < 0) >= 0:
        if x + y < k:
            res.append(x + y)
print(len(res), max(res))

