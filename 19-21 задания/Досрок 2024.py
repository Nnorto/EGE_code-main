from functools import *
@lru_cache(None)

def g(h):
    a, b = h
    m = [(a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)]
    if a + b >= 123:
        return 'win'
    if any(g(x) == 'win' for x in m):
        return 'p1'
    # or - если неудачный ход пети | and - если независимо от того как сходит петя
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v2'

for s in range(1, 110):
    a, b = 13, s
    h = a, b
    if g(h) == 'v2':
        print(b, g(h))

