from random import *
def fa(a):
    n = len(a)
    mins = 10 ** 10
    for i in range(len(a)):
        s = 0
        for j in range(len(a)):
            s += min(abs(j - i), n - abs(j - i)) * a[j]

        mins = min(mins, s)

    return mins


def fb(a):
    mins = 10 ** 19
    s = 0
    n = len(a)
    # бежим в первй раз
    for i in range(len(a)):
        s += a[i] * min(i, n - i)
    mins = s
    fs = bs = 0
    for i in range(1, n // 2 + 1):
        fs += a[i]

    bs = sum(a) - fs

    for i in range(1, len(a)):
        s = s - fs + bs
        fs += -a[i] + a[(n // 2 + i) % n]
        bs += a[i] - a[(n // 2 + i) % n]
        mins = min(mins, s)

    return mins

n = 6
k = 0

for test in range(100):
    a = [randrange(1, 100) for i in range(n)]
    k += 1
    resa, resb = fa(a), fb(a)
    if resa != resb:
        print('wrong', k)
        print(resa, resb)
        print(a)
        break