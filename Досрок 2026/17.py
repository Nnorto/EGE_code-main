f = open('17_28762.txt')
a = [int(x) for x in f]
b = [x for x in a if x % 23 == 0]
m = min(b)

res = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if x % m == 0 or y % m == 0:
        res.append(x + y)

print(len(res), max(res))