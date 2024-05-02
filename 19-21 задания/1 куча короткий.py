from functools import *
@lru_cache(None)
def g(h):
    if h >= 41:
        return "win"
    m = [h + 1, h + 10]
    if any(g(x) == 'win' for x in m): return "p1"
    if all(g(x) == 'p1' for x in m): return "v1"
    if any(g(x) == 'v1' for x in m): return "p2"
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return "v2"

for h in range(41, 0, -1):
    if g(h) == 'v2':
        print(h)
