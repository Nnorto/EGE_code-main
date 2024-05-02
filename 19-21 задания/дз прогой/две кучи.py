from functools import *
@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 263:
        return "win"
    m = [(a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)]
    if any(g(x) == 'win' for x in m): return "p1"
    if all(g(x) == 'p1' for x in m): return "v1"
    if any(g(x) == 'v1' for x in m): return "p2"
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return "v1orv2"


for x in range(1, 245 + 1):
    h = 17, x
    """if g(h) == 'v1':
        print(x, 'v1')"""
    if g(h) == 'p2':
        print(x, 'p2')
    if g(h) == 'v1orv2':
        print(x, 'v1orv2')

