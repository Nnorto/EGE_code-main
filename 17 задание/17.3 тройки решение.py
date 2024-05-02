f = open("17 файлы/17-3.txt")
a = []
for s in f:
    a.append(int(s))

count = 0
min_sr_ar = 10 ** 10
for i in range(len(a) - 2):
    if (abs(a[i]) % 14 == 0 or abs(a[i + 1]) % 14 == 0 or abs(a[i + 2]) % 14 == 0) \
            and (abs(a[i]) % 4 == 0 and abs(a[i + 1]) % 4 == 0 and abs(a[i + 2]) % 4 == 0):
        sr = (a[i] + a[i + 1] + a[i + 2]) // 3
        min_sr_ar = min(min_sr_ar, sr)
        count += 1

print(count, min_sr_ar)

# Ответ: 31 -7504
