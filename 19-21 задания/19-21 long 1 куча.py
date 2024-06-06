from functools import *
@lru_cache(None)
def g(h):
    if h >= 82:
        return "win"
    if g(h * 3) == 'win' or g(h + 4) == 'win' or g(h + 1) == 'win':  # Петя поб 1 ходом
        return 'p1'
    """ 
        Если в задании сказано что при любой игре Пети Ваня побеждает 1 ходом нужно использовать AND
        Если в задании сказано что Ваня побеждает 1 ходом ПРИ НЕУДАЧНОМ ХОДЕ Пети нужно использовать OR 
        |                                                   |
        ∨                                                   ∨
    """
    if g(h * 3) == 'p1' and g(h + 4) == 'p1' and g(h + 1) == 'p1':   # Ваня поб 1 ходом
        return "v1"

    """
        ∧                                                   ∧ 
        |                                                   |
    """

    if g(h * 3) == 'v1' or g(h + 4) == 'v1' or g(h + 1) == 'v1':   # Петя поб 2 х
        return "p2"
    if (g(h * 3) == 'p1' and g(h + 4) == 'p1' and g(h + 1) == 'p2') or \
            (g(h * 3) == 'p1' and g(h + 4) == 'p2' and g(h + 1) == 'p2'):
        return "v1orv2"

for x in range(1, 82):
    if g(x) == "v1":
        print(x)