f = open('17 файлы/17__1.txt')
a = [int(x) for x in f]
b = [x for x in a if len(str(abs(x))) == 5 and abs(x) % 100 == 42]
m = max(b)

res = []

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (abs(x) % 100 == 42 and len(str(abs(x))) == 5) + \
            (abs(y) % 100 == 42 and len(str(abs(y))) == 5) == 1:
        smk = x ** 2 + y ** 2
        if smk >= m ** 2:
            res.append(x + y)

print(len(res), max(res))
