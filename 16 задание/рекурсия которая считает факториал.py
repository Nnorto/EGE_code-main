from functools import *
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return n*f(n-1)

print(f(200))