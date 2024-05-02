from functools import *
@lru_cache(None)
def g(h):
    if h >= 43:
        return "win"
    m = [h + 1, h + 4, h * 3]
    if any(g(x) == 'win' for x in m): return "p1"
    if all(g(x) == 'p1' for x in m): return "v1"
    if any(g(x) == 'v1' for x in m): return "p2"
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return "v1orv2"

for h in range(42, 0, -1):
    if g(h) == 'v1':
        print(h, 'v1')
    if g(h) == 'p2':
        print(h, 'p2')
    if g(h) == 'v1orv2':
        print(h, 'v1orv2')
