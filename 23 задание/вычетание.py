from functools import *
@lru_cache(None)

def f(x, y):
    if x < y or x == 19 or x == 17:  # добавляется условие не содержит 19 и 17
        return 0
    if x == y:
        return 1
    return f(x - 3, y) + f(x - 2, y)


print(f(43, 7))
