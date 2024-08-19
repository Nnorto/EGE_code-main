from functools import lru_cache
@lru_cache(None)
def g(h):
    moves = [h + 1, h + 4, h * 3]
    if h >= 82:
        return 'ww'
    if any(g(x) == 'ww' for x in moves):
        return 'p1'
    if all(g(x) == 'p1' for x in moves):
        return 'v1'
    if any(g(x) == 'v1' for x in moves):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in moves):
        return 'v1orv2'


for h in range(1, 82):
    print(h, g(h))

# 19 задание ответ 27
# 20 задание ответ 9 23
# 21 задание ответ 22
