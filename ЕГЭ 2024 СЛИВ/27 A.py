f = open('2024_Файлы/27_B_2024.txt')
n = int(f.readline())
a = [int(x) for x in f]

maxs = -10 ** 100
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] > a[j] and a[k] > a[j]:
                maxs = max(maxs, a[i] - a[j] + a[k] - a[j])

print(maxs)
