f = open('27 файлы/27-B пары.txt')
n = int(f.readline())
s, minr = 0, 10**10
for p in f:
    a, b = map(int, p.split())
    raz = abs(a - b)
    s += max(a, b)
    if raz % 4 != 0:
        minr = min(minr, raz)

if s % 4 != 0:
    print(s)
else:
    print(s - minr)