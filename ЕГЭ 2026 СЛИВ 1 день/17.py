f = open('17.txt')
a = [int(s) for s in f]
res = []
m = min(x for x in a if x > 0 and x % 9 == 0)
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if x != y and abs(x - y) % m == 0:
        res.append(x+y)
print(len(res), max(res))