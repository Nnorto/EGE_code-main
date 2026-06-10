from functools import *

@lru_cache(10000)
def f(n):
    if n >= 19:
        return f(n - 4) + 3580
    if n < 19:
        return 6 * (g(n - 7) - 36)

@lru_cache(10000)
def g(n):
    if n >= 248_045:
        return n / 20 + 28
    if n < 248_045:
        return g(n + 9) - 4

for i in range(248_245, 1, -1):
    g(i)
for i in range(1, 673+1):
    f(i)
print(f(673))