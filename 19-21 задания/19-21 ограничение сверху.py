from functools import *

@lru_cache(None)
def g(h):
    m = []
    if h * 3 <= 83:
        m.append(h*3)
    if h + 2 <= 83:
        m.append(h+2)
    if 34 <= h <= 83:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v2'

for h in range(1, 34):
    if g(h) == 'p2':
        print(h, g(h))