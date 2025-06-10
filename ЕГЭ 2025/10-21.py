from functools import *
@lru_cache(None)

def g(h):
    m = [h - 2, h // 2] # ceil(h / 2) -  если просят окр до БОЛЬШЕГО
    if h <= 87:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1' # 19 задание
    if any(g(x) == 'v2' for x in m):
        return 'p2' # 20 задание
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2' # 21 задание

for s in range(89, 500):
    if g(s) == 'v1':  # меняем тут
        print(s)