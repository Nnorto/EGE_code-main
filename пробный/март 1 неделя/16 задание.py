from functools import *
@lru_cache()

def f(n):
    if 0 < n <= 1:
        return 1
    return (n + 1) * f(n - 1)

print(f(200)//f(198))