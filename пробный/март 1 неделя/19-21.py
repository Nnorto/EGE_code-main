"""
1 ≤ S ≤ 45
>= 46
+1 *3
"""
from functools import lru_cache


def moves(h):
    return (h + 2), (h + 3), (h + 4), (h * 2)


@lru_cache(None)
def game(h):
    if h >= 229:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):
        return "V1"
    if any(game(m) == "V1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "V2"


for x in range(1, 229):
    if game(x) == 'V1':
        print(x, game(x))

    if game(x) == 'P2':
        print(x, game(x))
    if game(x) == 'V2':
        print(x, game(x))