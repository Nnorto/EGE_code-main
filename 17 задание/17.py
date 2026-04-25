f = open('17 файлы/17statokt23.txt')
a = [int(x) for x in f]
b = [x for x in a if abs(x) % 100 == 17]
m = max(b)
res = []
for i in range(len(a) - 2):
    x, y, z = a[i], a[i + 1], a[i + 2]
    if (len(str(abs(x))) == 4) + \
            (len(str(abs(y))) == 4) + \
            (len(str(abs(z))) == 4) == 2:
        if (x % 5 == 0) + \
                (y % 5 == 0) + \
                (z % 5 == 0) >= 1:
            sm = x + y + z
            if sm > m:
                res.append(sm)
print(len(res), max(res))
