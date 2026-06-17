from functools import lru_cache
from math import ceil
@lru_cache(None)
def g(h):
    a, b = h

    m = [(a - 1, b), (a, b - 1)]
    if a > 1:
        m.append((ceil(a // 2), b))
    if b > 1:
        m.append((a, ceil(b // 2)))

    if a + b <= 40:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(21, 300):
    h = 20, s
    # if g(h) == 'v1':
    #     print(s)
    # 19z - 83

    # if g(h) == 'p2':
    #     print(s)
    # 20z - 43, 85

    if g(h) == 'v1orv2':
        print(s)
    # 21z - 45