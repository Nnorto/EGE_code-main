f = open('17_19249.txt')
a = [int(x) for x in f]
maxel = max([x for x in a if abs(x) % 100 == 43 and len(str(abs(x))) == 5])
count = 0
mins = 10**10
for i in range(len(a) - 2):
    if (len(str(abs(a[i]))) == 5 and abs(a[i]) % 100 == 43) or \
            (len(str(abs(a[i + 1]))) == 5 and abs(a[i + 1]) % 100 == 43) or \
            (len(str(abs(a[i + 2]))) == 5 and abs(a[i + 2]) % 100 == 43):
        s = a[i] ** 2 + a[i + 1] ** 2 + a[i + 2] ** 2
        if s <= maxel ** 2:
            count += 1
            mins = min(mins, s)

print(count, mins)