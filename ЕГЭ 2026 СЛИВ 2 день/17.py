f = open('17.txt')
a = [int(x) for x in f]
res = []
m3 = max([x for x in a if abs(x) % 10 == 3])
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 1]
    if (x + y + z) % m3 == 0:
        res.append(x + y + z)
print(len(res), max(res))