f = open('../file17/17.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if abs(x) % 100 == 25]
m = max(b)
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if (len(str(abs(x))) == 4) \
            + (len(str(abs(y))) == 4) \
            + (len(str(abs(z))) == 4) >= 2:
        if x + y + z <= m:
            print(x, y, z)
            res.append(x + y + z)

print(len(res), max(res))
