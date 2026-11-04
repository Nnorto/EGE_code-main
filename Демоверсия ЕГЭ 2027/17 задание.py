f = open('demo_17.txt')
a = [int(x) for x in f]
res = []
m = min(a)
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if x % 33 == m or y % 33 == m:
        res.append(x + y)
print(len(res), max(res))