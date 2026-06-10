from functools import *

@lru_cache(1000)
def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * f(n - 4)

for i in range(1, 13_770):
    if i == 13766:
        a = f(i)
    elif i == 13762:
        b = f(i)
    elif i == 13758:
        c = f(i)
    f(i)

print((a - 9 * b) / c)