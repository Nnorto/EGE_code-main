from functools import *
@lru_cache()

def f(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n <= 25 and n % 3 == 0:
        return f(n + 1) + 2 * f(n + 4)
    return f(n + 2) + 3 * f(n + 5)

count = 0
for n in range(1, 1000+1):
    summa = sum(list(map(int, str(f(n)))))
    if summa == 24:
        count += 1
print(count)

# или
def f(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n <= 25 and n % 3 == 0:
        return f(n + 1) + 2 * f(n + 4)
    if n <= 25 and n % 3 != 0:
        return f(n + 2) + 3 * f(n + 5)

def summap(n):
    s = str(n)
    return sum(list(map(int, s)))
def summas(n):
    s = str(n)
    a = []
    for i in s:
        a.append(int(i))
    return sum(a)
def sumgen(n):
    s = str(n)
    a = [int(i) for i in s]
    return sum(a)
def sumwhile(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


c = 0
for n in range(1, 1000+1):
    if sumgen(f(n)) == 24:
        c += 1
print(c)