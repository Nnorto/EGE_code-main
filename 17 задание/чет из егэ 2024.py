f = open('17 файлы/17_16383.txt')
a = [int(x) for x in f]
max5z21 = max([x for x in a if abs(x) % 100 == 21 if 10000 <= abs(x) <= 99999])
count = 0
maxs = -10000000
for i in range(len(a)-1):
    if ((abs(a[i]) % 100 == 21) and (9999 < abs(a[i]) < 100_000)) \
            + ((abs(a[i+1]) % 100 == 21) and (9999 < abs(a[i+1]) < 100_000)) == 1:
        sk = a[i] ** 2 + a[i+1] ** 2
        if sk >= max5z21**2:
            count += 1
            maxs = max(maxs, a[i] + a[i+1])

print(count, maxs)

f = open('17 файлы/17_16383.txt')
a = [int(x) for x in f]
max5z21 = max([x for x in a if abs(x) % 100 == 21 if 10000 <= abs(x) <= 99999])
count = 0
maxs = 0
for i in range(len(a) - 1):
    if (len(str(abs(a[i]))) == 5 and str(a[i])[-2:] == '21') \
            + (len(str(abs(a[i + 1]))) == 5 and str(a[i+1])[-2:] == '21') == 1:
        sk = a[i] ** 2 + a[i + 1] ** 2
        if sk >= max5z21**2:
            count += 1
            maxs = max(maxs, a[i] + a[i + 1])

print(count, maxs)

f = open('17 файлы/17_16383.txt')
a = [int(x) for x in f]
max5z21 = max([x for x in a if abs(x) % 100 == 21 if 10000 <= abs(x) <= 99999])
count = 0
maxs = 0
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if (abs(x) % 100 == 21 and 9999 < abs(x) < 100_000) != (abs(y) % 100 == 21 and 9999 < abs(y) < 100_000):
        sk = a[i] ** 2 + a[i + 1] ** 2
        if sk >= max5z21**2:
            count += 1
            maxs = max(maxs, a[i] + a[i + 1])

print(count, maxs)




f = open('17 файлы/17_16383.txt')
a = [int(x) for x in f]
max5z21 = max([x for x in a if abs(x) % 100 == 21 if 10000 <= abs(x) <= 99999])
count = 0
maxs = 0

for i in range(len(a) - 1):
    if (abs(a[i] % 100) == 21 and 9999 < abs(a[i]) < 100000) and (
            abs(a[i + 1] % 100) != 21 and (abs(a[i + 1]) < 9999 or abs(a[i + 1]) > 100000)) or (
            abs(a[i + 1] % 100) == 21 and 9999 < abs(a[i + 1]) < 100000) and (
            abs(a[i] % 100) != 21 and (abs(a[i]) < 9999 or abs(a[i]) > 100000)):
        if a[i]**2 + a[i+1]**2 >= 99921 ** 2:
            count += 1
            maxs = max(maxs, a[i] + a[i + 1])

print(count, maxs)