from functools import *

@lru_cache(None)

def g(h):
    m = [h - 3, h - 7, h // 3]  # ceil(h/3) - округ в большую
    if h <= 11:
        return 'w'
    if any(g(x) == 'w' for x in m): return 'p1'
    if all(g(x) == 'p1' for x in m): return 'v1'
    if any(g(x) == 'v1' for x in m): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return 'v1orv2'

for s in range(12, 500):
    if g(s) == 'v1':
        print(s)




from functools import *

@lru_cache(None)

def g(h):
    a, b = h
    m = [(a-3, b), (a, b - 3), (a-7, b), (a, b - 7), (a // 3, b), (a, b // 3)]  # ceil(h/3) - округ в большую
    if a > 0 and b > 0:
        if a + b <= ...:
            return 'w'
        if any(g(x) == 'w' for x in m): return 'p1'
        if all(g(x) == 'p1' for x in m): return 'v1'  # если неудачный ход то all меняем на any ТОЛЬКО В 19 ЗАДАНИИ
        if any(g(x) == 'v1' for x in m): return 'p2'
        if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return 'v1orv2'

for s in range(...):
    h = ..., s
    if g(h) == '...':
        print(s)
