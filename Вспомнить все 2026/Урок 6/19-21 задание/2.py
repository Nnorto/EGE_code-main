from functools import lru_cache

@lru_cache(None)
def g(h):
    a, b = h
    m = [(a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)]
    if a + b >= 62:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 54+1):
    h = 7, s
    # if g(h) == 'v1':
    #     print(s)
    #     break

    # 19z - 14

    # if g(h) == 'p2':
    #     print(s)
    #     break

    # 20z - 23

    if g(h) == 'v1orv2':
        print(s)

    # 21z - 21, 24