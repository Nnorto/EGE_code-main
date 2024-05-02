from functools import *
@lru_cache(None)
def g(h):
    a, b = h  # Создаем два числа, (две кучи)
    m = [(a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)]   # Всевозможные ходы
    if a + b >= 259: return "win" # Сумма при которой засчитывается победа
    if any(g(x) == 'win' for x in m): return 'p1'  # Петя поб 1 ч
    if all(g(x) == 'p1' for x in m): return "v1"   # Ваня поб после хода пети
    if any(g(x) == 'v1' for x in m): return 'p2'   # Петя поб 2 х
    if all(g(x) == "p1" or g(x) == "p2" for x in m): return "v1orv2"  # ваня поб или 1 или 2 ходом


for s in range(1, 241+1):
    h = 17, s   # наши камни из задания
    if g(h) == "v1orv2":  # меняем в зависимости от задания
        print(s)