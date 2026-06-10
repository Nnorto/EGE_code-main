from functools import *

@lru_cache(1000)
def f(n):
    if n == 1:
        return 2
    if n >= 2:
        return f(n - 1) - g(n - 1)

@lru_cache(1000)
def g(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) + g(n - 1)

for i in range(1, 15):
    f(i)
for i in range(1, 15):
    g(i)

print(f(5)/g(5))