f = open('17.txt')
a = [int(x) for x in f]
# b = [x for x in a if len(str(x)) == 3 and str(x)[-1] == '7']
b = [x for x in a if 100 <= x <= 999 and x % 10 == 0]
res = []
for i in range(len(a) - 1):
    if (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) == 1:
        sm = a[i] + a[i + 1]
        if sm % min(b):
            res.append(sm)

print(len(res), min(res))
