from functools import *


@lru_cache(1000)
def f(n):
    return 3 * g(n - 3) + 7


@lru_cache(1000)
def g(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return g(n - 3) + 1


for i in range(1, 38_000):
    g(i)

for i in range(1, 38_000):
    if i == 37811:
        a = f(i)
    else:
        f(i)

print(a)