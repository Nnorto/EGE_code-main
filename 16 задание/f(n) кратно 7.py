from functools import *
@lru_cache()

def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return n + 3 + f(n - 1)
    return n * n + f(n - 2)

count = 0
for n in range(1, 1000+1):
    if f(n) % 7 == 0:
        count += 1
print(count)
