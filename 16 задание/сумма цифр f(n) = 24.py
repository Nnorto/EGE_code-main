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
