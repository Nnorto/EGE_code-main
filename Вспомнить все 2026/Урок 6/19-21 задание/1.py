from functools import lru_cache

@lru_cache(None)
def g(h):
    m = [h - 1, h - 5, h // 3]
    if h <= 10:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1'for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(11, 300):
    # if g(s) == 'v1':
    #     print(s)
    # 19z - 33
    # if g(s) == 'p2':
    #     print(s)
    # 20z - 34, 101
    if g(s) == 'v1orv2':
        print(s)
    # 21z - 35