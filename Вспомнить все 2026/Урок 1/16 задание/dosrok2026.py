from functools import *


@lru_cache(1000)
def f(n):
    if n < 10:
        return 3

    if n >= 10:
        return (n + 4) * f(n - 5)


a, b, c = 0, 0, 0
for i in range(1, 257500):
    if i == 257487:
        a = f(i)
    elif i == 257477:
        b = f(i)
    elif i == 257472:
        c = f(i)
    else:
        f(i)
print((a // 683 + 67 * b) // c)
