from functools import *
@lru_cache(None)
def f(x, y, kch, knch):
    if x > y or (knch >= kch and x == y):
        return 0
    if x == y and kch > knch:
        return 1
    if x % 2 == 0:
        return f(x + 2, y, kch + 1, knch) + f(x + 3, y, kch, knch+1)  + f(x * 4, y, kch + 1, knch)
    if x % 2 != 0:
        return f(x + 2, y, kch, knch+1) + f(x + 3, y, kch+1, knch) + f(x * 4, y, kch + 1, knch)

res = f(1, 100, 0, 1)
print(sum(map(int, str(res))))