f = open('17_19249.txt')
a = [int(x) for x in f]
ctn = 0
mins = 10**10
maxel = max([x for x in a if len(str(abs(x))) == 5 and abs(x) % 100 == 43])

for i in range(len(a) - 2):
    if (len(str(abs(a[i]))) == 5 and abs(a[i]) % 100 == 43)\
            + (len(str(abs(a[i + 1]))) == 5 and abs(a[i + 1]) % 100 == 43)\
            + (len(str(abs(a[i + 2]))) == 5 and abs(a[i + 2]) % 100 == 43) >= 1:
        sm = a[i] ** 2 + a[i + 1] ** 2 + a[i + 2] ** 2
        if sm <= maxel**2:
            ctn += 1
            mins = min(mins, sm)
print(ctn, mins)