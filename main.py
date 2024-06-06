from functools import *
@lru_cache(None)

def g(h):
    if h >= 435:
        return 'w'
    m = [h + 5, h * 3]
    if any(g(x) == 'w' for x in m): return 'p1'
    if all(g(x) == 'p1' for x in m): return 'v1'
    if any(g(x) == 'v1' for x in m): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return 'v2orv1'


for h in range(1, 435):
    print(g(h), h)
