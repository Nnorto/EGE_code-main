f = open('17.txt')

a = [int(x) for x in f]
b = [x for x in a if abs(x) % 100 == 0]
res = []
for i in range(len(a) - 2):
    if (9<abs(a[i])<100) + (9<abs(a[i])<100) + (9<abs(a[i])<100) == 1:
        sm = a[i] + a[i+1] + a[i + 2]
        if sm > max(b):
            res.append(sm)

print(len(res), max(res))