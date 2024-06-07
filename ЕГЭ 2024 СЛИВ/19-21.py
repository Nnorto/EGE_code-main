from functools import *
@lru_cache(None)
def g(h):
    m = [h + 1, h * 2]
    if h >= 69:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == "p2" for x in m):
        return 'v1orv2'

for h in range(1, 69):
    print(g(h), h)

"""
Ответы: 
19: 34
20: 17 33
21: 32
"""