from functools import *
@lru_cache(None)
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x // 3, y) + f(x - 1, y) + f(x - 5, y)

print(f(46,22)*f(22,5))

