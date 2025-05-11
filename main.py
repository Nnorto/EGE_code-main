from functools import *
@lru_cache(None)
def g(h):
    if h>=211: return 'win'
    m=[h+1,h+3,h*4]
    if any(g(x) == 'win' for x in m): return 'p1'
    if all(g(x) == 'p1' for x in m): return 'v1'
    if any(g(x) == 'v1' for x in m): return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in m): return 'v1orv2'
    if any(g(x) == 'p2' for x in m): return 'v2'
    if any(g(x) == 'v2' for x in m): return 'p3'
for x in range(1,210+1):
    if g(x) == 'p3':
        print((g(x)),x)