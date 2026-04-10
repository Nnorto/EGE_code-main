from functools import *
@lru_cache(None)
def g(h):
    m = [h - 3, h - 7, h // 3]
    if h <= 11:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(13, 500):
    if g(s) == 'p2':  # v1 - 19 задание /  p2 - 20 задание / v1orv2 - 21 задание
        print(s)

# 19 задание - 36
# 20 задание - 39 40
# 21 задание - 42
