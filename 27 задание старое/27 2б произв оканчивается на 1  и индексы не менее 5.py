f = open('27 файлы/27-B.txt')
n = int(f.readline())
a = [int(x) for x in f]

res = k1 = k3 = k7 = k9 = 0
k = 5

for i in range(k, len(a)):
    if a[i - k] % 10 == 1:
        k1 += 1
    if a[i - k] % 10 == 3:
        k3 += 1
    if a[i - k] % 10 == 7:
        k7 += 1
    if a[i - k] % 10 == 9:
        k9 += 1

    if a[i] % 10 == 1:
        res += k1
    if a[i] % 10 == 3:
        res += k3
    if a[i] % 10 == 7:
        res += k7
    if a[i] % 10 == 9:
        res += k9

print(res)

#ответ для В 41085342933