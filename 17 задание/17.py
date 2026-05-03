f = open('17 файлы/17-1.txt')
a = [int(x) for x in f]
res = []

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if x % 3 == 0 or y % 3 == 0:
        if x + y <= max(x for x in a if x % 3 == 0):
            res.append(x + y)

print(len(res), max(res))

f = open('17 файлы/17-1.txt')
data = [int(x) for x in f]
count = 0
maxpairsum = 0
maxmult3 = max(x for x in data if x % 3 == 0)
for i in range(len(data)-1):
    a = data[i]
    b = data[i + 1]
    if (a % 3 == 0 or b % 3 == 0) and (a + b <= maxmult3):
        count +=1
        maxpairsum = max(maxpairsum, a + b)
print(count, maxpairsum)
