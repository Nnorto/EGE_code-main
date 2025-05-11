f = open('27 файлы/27-B.txt')
n = int(f.readline())
a = [int(x) for x in f]
res = k7ch = k7nch = k1ch = k1nch = 0
k = 5

for i in range(k, len(a)):
    if a[i - k] % 7 == 0 and a[i - k] % 2 == 0:
        k7ch += 1
    elif a[i - k] % 7 == 0 and a[i - k] % 2 != 0:
        k7nch += 1
    elif a[i - k] % 7 != 0 and a[i - k] % 2 == 0:
        k1ch += 1
    elif a[i - k] % 7 != 0 and a[i - k] % 2 != 0:
        k1nch += 1

    if a[i] % 7 == 0 and a[i] % 2 == 0:
        res += k7ch + k1ch
    elif a[i] % 7 == 0 and a[i] % 2 != 0:
        res += k7nch + k1nch
    elif a[i] % 7 != 0 and a[i] % 2 == 0:
        res += k7ch
    elif a[i] % 7 != 0 and a[i] % 2 != 0:
        res += k7nch

print(res)