from functools import *
@lru_cache(1000)
def f(n):
    if n < 10:
        return n
    if n >= 10 and n % 2 == 0:
        return n + f(n - 3)
    if n >= 10 and n % 2 != 0:
        return 1 + f(n - 1)

for i in range(1, 2666):
    f(i)
print(f(2566)/f(2557))