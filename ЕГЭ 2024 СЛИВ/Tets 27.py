def B(m):
    m1 = m2 = m3 = -10**100
    a = m
    for i in range(n - 2):
        m1 = max(m1, a[i - 2])
        m2 = max(m2, m1 - 2 * a[i - 1])
        m3 = max(m3, m2 + a[i])
    return m3

def A(m):
    a = m
    maxs = -10 ** 100
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if a[i] > a[j] and a[k] > a[j]:
                    maxs = max(maxs, a[i] - a[j] + a[k] - a[j])

    return maxs

from  random import *
n = 100
for i in range(100):
    a = [randrange(1, 10) for x in range(n)]
    resA = A(a)
    resB = B(a)
    if resA != resB:
        print('wrong')
        print(a, resA, resB)
        break
