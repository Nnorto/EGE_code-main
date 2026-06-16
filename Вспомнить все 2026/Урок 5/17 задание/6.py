f = open('../file17/17_22.txt')
a = [int(s) for s in f]
res = []
m = min(a)
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if (x % 18) + (y % 18) == m:
        res.append(x + y)

print(len(res), max(res))

