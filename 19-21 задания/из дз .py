from functools import *
@lru_cache(None)

def g(h):

    m = [h+1, h+4, h*3]
    if h >= 43:
        return 'win'
    if any(g(x) == 'win' for x in m):
        return 'p1'
    # or - если неудачный ход пети | and - если независимо от того как сходит петя
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    # if (g(h * 3) == 'p1' and g(h + 4) == 'p2' and g(h + 1) == 'p2') \
    #         or (g(h * 3) == 'p1' and g(h + 4) == 'p1' and g(h + 1) == 'p2'):
    #     return 'v2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v2'


for s in range(1, 42):
    if g(s) == 'v2':
        print(g(s), s)

