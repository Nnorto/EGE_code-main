from functools import *
@lru_cache(None)
def g(h):
    if h >= 41:
        return "win"
    if g(h+1) == 'win' or g(h+10) == 'win':
        return "p1"
    if g(h+1) == 'p1' and g(h+10) == 'p1':
        return 'v1'
    if g(h+1) == 'v1' or g(h+10) == 'v1':
        return 'p2'
    if (g(h+1) == 'p1' and g(h+10) == 'p2') or (g(h+1) == 'p2' and g(h+10) == 'p1'):
        return 'v2orv1'

for h in range(41, 0, -1):
    if g(h) == 'v2orv1':
        print(h)
