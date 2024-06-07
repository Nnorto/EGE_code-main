f = open('2024_Файлы/17 реальное.txt')
a = [int(x) for x in f]
minel = min(a)
c = maxs = 0
for i in range(len(a) - 1):
    if a[i] % 18 + a[i + 1] % 18 == minel:
        c += 1
        maxs = max(maxs, a[i] + a[i +1])


print(c, maxs)