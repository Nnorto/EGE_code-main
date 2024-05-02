from functools import *
@lru_cache()

def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return f(n - 1) + 2 * f(n // 2)
    return f(n - 1) + f(n - 3)

count = 0
for n in range(1, 100):
    if f(n) < 10**8:
        count += 1
print(count)
