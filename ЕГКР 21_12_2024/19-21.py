from functools import lru_cache
@lru_cache(None)
def g(h):
    m = [h + 3, h + 6, h * 3]
    if h >= 132:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'
for h in range(1, 132):
    if g(h) == 'v1orv2':
        print(h)