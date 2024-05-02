f = open("Файлы/26_ege22_den1_8.txt")
n = int(f.readline())
a = [int(x) for x in f]
a.sort(reverse=True)
t_box = a[0]
count = 1
for i in range(n):
    if t_box - a[i] >= 11:
        t_box = a[i]
        count += 1


print(count, t_box)