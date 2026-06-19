from functools import lru_cache
@lru_cache(None)
def g(h):
    a, b = h
    m = [(a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)]
    if a + b >= 155:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 139+1):
    h = 15, s
    # if g(h) == 'v1':
    #     print(s)
    #     break
    # if g(h) == 'p2':
    #     print(s)
    if g(h) == 'v1orv2':
        print(s)
        break