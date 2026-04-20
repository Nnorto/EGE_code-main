f = open('17.txt')

a = [int(x) for x in f]
res = []
m = max([x for x in a if abs(x) % 100 == 28])
print(m)

for i in range(len(a) - 2):
    x, y, z = a[i], a[i + 1], a[i + 2]
    if (len(str(abs(x))) == 3) \
            + (len(str(abs(y))) == 3) \
            + (len(str(abs(z))) == 3) >= 1:
        sr = (x + y + z) / 3
        if sr > 0 and sr < m:
            res.append(x + y + z)

print(len(res), max(res))

# 1290 193483