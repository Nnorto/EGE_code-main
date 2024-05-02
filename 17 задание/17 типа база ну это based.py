f = open('17 файлы/17-1.txt')
a = f.read().splitlines()
a = list(map(int, a))

min = 1000000
count = 0
max_dif = 0
for x in range(10001):
    if x % 2 != 0 and x < min:
        min = x

for i in range(len(a) - 1):
    dif = abs(a[i] - a[i + 1])
    if ((a[i] % 3 == 0 and a[i + 1] % 3 != 0) or (a[i] % 3 != 0 and a[i + 1] % 3 == 0)) and dif < min:
        count += 1
        if dif > max_dif:
            max_dif = dif


print(count, max_dif)