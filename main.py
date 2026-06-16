from functools import *

@lru_cache(None)
def g(h):
    a, b = h
    m = [(a + 4, b), (a, b + 4), (a * 3, b), (a, b * 3)]
    if a + b >= 154:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v1orv2'

for s in range(1, 142+1):
    h = 11, s
    if g(h) == 'v1orv2':
        print(s)
        break



# 19 задание 'v1' - Ваня выиграет первым ходом
# 20 задание 'p2' - Петя выиграет вторым ходом
# 21 задание 'v1orv2' - Ваня выиграет первым ходом или вторым ходом