f = open("Файлы/26_ege22_den1_8.txt")
n = int(f.readline())
a = list(map(int, f))
a.sort(reverse=True)
tk = a[0]
count = 1
for i in range(len(a)):
    if a[i] <= tk - 11:
        tk = a[i]
        count += 1

print(count, tk)
