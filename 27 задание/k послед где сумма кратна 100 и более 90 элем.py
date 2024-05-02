f = open('27 файлы/27-B1.txt')
n = int(f.readline())
a = [int(x) for x in f]
si = res = 0
ke = 90
k = 100
prefs = [0] * k

for i in range(ke):
    si += a[i]

for i in range(ke, len(a)):
    si += a[i]
    if si % 100 == 0:
        res += 1
    res += prefs[si % k]

print(res)

# 11218606901