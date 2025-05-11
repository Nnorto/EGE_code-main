f = open('27 файлы/27-B1.txt')
n = int(f.readline())
a = [int(x) for x in f]
mins = 10**10
s = 0
for i in range(len(a)):
    s += a[i] * min(i, n - i)

mins = s

fs = 0
for i in range(1, len(a)//2 + 1):
    fs += a[i]

bs = sum(a) - fs
for i in range(1, len(a)):
    s = s - fs + bs
    fs += -a[i] + a[(i + n // 2)%n]
    bs += a[i] - a[(i + n // 2)%n]
    mins = min(mins, s)
print(mins)