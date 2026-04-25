f = open('17 файлы/17__2.txt')
a = [int(x) for x in f]

b = [x for x in a if len(str(abs(x))) == 4]
m = max(b)

res = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) == 1:
        pr = x * y
        if pr % m == 0:
            res.append(pr)

print(len(res), abs(min(res)))