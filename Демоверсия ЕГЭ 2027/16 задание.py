from functools import lru_cache
@lru_cache(1000)
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)
for i in range(1, 3100): f(i)
print((f(3038) + 5 * f(3037)) / f(3036))