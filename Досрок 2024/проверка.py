mins = 10**19
s = 0
a = [85, 93, 15, 11, 25, 96]
n = len(a)
# бежим в первй раз
for i in range(len(a)):
    s += a[i] * min(i, n - i)

mins = s
print('***', s)

fs = bs = 0
for i in range(1, n // 2 + 1):
    fs += a[i]

bs = sum(a) - fs

for i in range(1, len(a)):
    s = s - fs + bs
    fs += -a[i] + a[(n // 2 + i) % n]
    bs += a[i] - a[(n // 2 + i) % n]
    mins = min(mins, s)
    print('***', s)

print('***', mins)


mins = 10**10
for i in range(len(a)):
    s = 0
    for j in range(len(a)):
        s += min(abs(j - i), n - abs(j - i)) * a[j]

    mins = min(mins, s)
    print(s)


print(mins)
