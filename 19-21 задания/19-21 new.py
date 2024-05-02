"""
1 ≤ S ≤ 45
>= 46
+1 *3
"""
from functools import lru_cache


def moves(h):
    return (h + 1), (h * 3)


@lru_cache(None)
def game(h):
    if h >= 46:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):
        return "V1"
    if any(game(m) == "V1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "V2"


for x in range(1, 46):
    if game(x) is not None:
        print(x, game(x))