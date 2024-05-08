f = open('1_27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
mins = 10**19
s = 0
# бежим в первй раз
for i in range(len(a)):
    s += a[i] * min(i, n - i)

fs = bs = 0
for i in range(1, n // 2 + 1):
    fs += a[i]

bs = sum(a) - fs

for i in range(1, len(a)):
    s = s - fs + bs
    fs += -a[i] + a[(n // 2 + i)%n]
    bs += a[i] - a[(n // 2 + i)%n]
    mins = min(mins, s)

print(mins)