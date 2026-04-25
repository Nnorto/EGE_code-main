f = open('test.txt')
a = [int(x) for x in f]

res = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if x % 3 == 0 or y % 3 == 0:
        res.append(x+y)
print(len(res), max(res))