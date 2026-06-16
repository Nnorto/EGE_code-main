f = open('../file17/17-1.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if len(str(abs(x))) == 2 and abs(x) % 10 == 4]
m = min(b)
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if (len(str(abs(x))) == 2) + (len(str(abs(y))) == 2) == 1:
        s = x + y
        if s % m == 0:
            res.append(x + y)
print(len(res), max(res))
