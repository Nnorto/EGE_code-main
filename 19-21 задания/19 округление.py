"""
19 задание
x – 1 куча
y – 2 куча
p – чей ход
"""
from math import ceil
"""
ceil() -> в большую сторону -> 9 / 2 = 5
floor() -> в меньшую 9 / 2 = 4 
"""


def f(x, y, p):
    if x + y <= 40 and p == 2:
        return True
    if x + y > 40 and p == 2:
        return False
    return f(x - 1, y, p + 1) or f(x, y - 1, p + 1) or f(x // 2, y, p + 1) or f(x, y // 2, p + 1)


for s in range(21, 1000):  # Диапазон S
    if f(20, s, 0):  # 0 - ничей ход, 1 – Петя, 2 – Ваня, 3 – Петя, 4 - Ваня
        print(s)
