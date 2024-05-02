f = open('17 файлы/17stat_dek23.txt')
a = [int(x) for x in f]
min3 = max([int(x) for x in a if abs(x) % 1000 == 321])

res = []
for i in range(len(a)-2):
    if (10000 <= a[i] <= 99999)+ (10000 <= a[i+1] <= 99999) + (10000 <= a[i+2] <= 99999) == 2:
        if (a[i] % 5 == 0) + (a[i+1] % 5 == 0) + (a[i+2] % 5 == 0) >= 1:
            s = a[i] + a[i+1] + a[i+2]
            if s > min3:
                res.append(s)

print(len(res), max(res))
