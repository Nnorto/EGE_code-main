from functools import *

@lru_cache(1000)
def f(n):
    if n < 5:
        return 1 + 2*n
    if n % 3 == 0:
        return 2 * (n + 1) * f(n - 2)
    return 2 * n + 1 + f(n - 1) + 2 * f(n - 2)

for i in range(0, 15+1):
    f(i)

print(f(15))