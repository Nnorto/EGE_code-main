from functools import *
@lru_cache(None)
def g(h):
    a, b = h
    m = [(a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)]
    if a + b >= 65:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 59):
    h = 6, s
    if g(h) == 'v1orv2':
        print(s)
# 19 - 7
# 20 - 10 19
# 21 -