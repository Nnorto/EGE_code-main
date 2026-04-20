from functools import lru_cache


@lru_cache()
def g(h):
    m = [h + 1, h + 5, h * 3]
    if h >= 124:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 123+1):
    if g(s) == 'v1orv2':
        print(s)

# 19 задание: 41
# 20 задание: 36 40
# 21 задание: 35