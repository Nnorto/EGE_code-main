from functools import *

@lru_cache(10000)
def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    if n < 21:
        return 10 * (g(n - 7) - 36)

@lru_cache(10000)
def g(n):
    if n >= 22560:
        return n / 23 + 33
    if n < 22560:
        return g(n + 11) - 4

for i in range(22770, 1, -1):
    g(i)
for i in range(1, 548+1):
    f(i)

print(f(548))
