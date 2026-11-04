from functools import lru_cache
@lru_cache(None)
def g(h):
    a, b = h
    m = [(a + 4, b), (a, b + 4), (a * 2, b), (a, b * 2)]
    if a + b >= 133:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if any(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 115+1):
    h = 17, s
    if g(h) == 'v1':
        print(s)

# 19z -- 56
# 20z -- 28 48
# 21z -- 44
