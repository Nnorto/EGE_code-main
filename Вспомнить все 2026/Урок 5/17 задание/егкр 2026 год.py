f = open('../file17/17_27301.txt')
a = [int(s) for s in f]
res = []
b = [x for x in a if str(abs(x))[:2] == '45']
m = max(b)
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if (x < 0) + (y < 0) + (z < 0) == 1:
        if x + y + z >= m:
            res.append(x + y + z)
r = [x for x in res if abs(x) % 100 == 45]
print(len(res), min(r))