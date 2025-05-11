f = open("/27 задание старое/27 файлы/27_A_1_day.txt")
k = int(f.readline())
N = f.readline()
a = list(map(int, f))
minc = 10 ** 10
for i in range(len(a)):
    for j in range(i + k, len(a)):
        for q in range(j + k, len(a)):
            minc = min(minc, a[i] + a[j] + a[q])
print(minc)
