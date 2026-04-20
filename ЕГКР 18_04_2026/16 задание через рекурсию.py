from functools import lru_cache


@lru_cache()
def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    if n < 21:
        return 10 * (g(n - 7) - 36)


@lru_cache()
def g(n):
    if n >= 22560:
        return n / 23 + 33
    if n < 22560:
        return g(n + 11) - 4

for x in range(22590, 0, -1):
    g(x)

for x in range(600):
    f(x)

print(f(548))

