f = open('../file17/17.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if x % 2 == 0]
m = min(b)

for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if x % 3 == 0 or y % 3 == 0:
        if x + y > m:
            res.append(x + y)
print(len(res), max(res))