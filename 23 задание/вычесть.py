from functools import *
@lru_cache(None)

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 3, y) + f(x - 2, y) + f(x - 1, y)


print(f(36,28) * f(28,26) * f(26,13))
