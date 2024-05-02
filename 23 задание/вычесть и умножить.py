from functools import *
@lru_cache(None)

def f(x, y, a):
    if x > y + 1:  # мы можем перепрыгнуть и вычесть
        return 0
    if x == y:
        return 1
    if a == 1:
        return f(x * 2, y, 0) + f(x * 3, y, 0)
    return f(x - 1, y, a + 1) + f(x * 2, y, 0) + f(x * 3, y, 0)



print(f(3, 15, 0))
