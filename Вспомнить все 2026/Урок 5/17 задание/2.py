f = open('../file17/17.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if x % 10 == 0]
m = max(b)
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if x % 5 == 0 and y % 5 == 0 and z % 5 == 0:
        if x + y + z <= m:
            res.append(x + y + z)

print(len(res), max(res))