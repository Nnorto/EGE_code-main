f = open('../file17/17_21.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if len(str(abs(x))) == 5 and abs(x) % 100 == 43]
m = max(b)

for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if (len(str(abs(x))) == 5 and abs(x) % 100 == 43) \
            + (len(str(abs(y))) == 5 and abs(y) % 100 == 43) \
            + (len(str(abs(z))) == 5 and abs(z) % 100 == 43) >= 1:
        s = x*x + y*y + z*z
        if s <= m ** 2:
            res.append(s)
print(len(res), min(res))

