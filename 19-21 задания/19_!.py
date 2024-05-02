"""
19 задание
x – 1 куча
p – чей ход
"""


def f(x, y, p):
    if x + y >= 59 and (p == 2 or p == 4):
        return True
    if x + y < 59 and p == 4:
        return False
    if x + y >= 59:
        return False
    if p % 2 == 1:
        return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)


for i in range(1, 54): # Диапазон S
    if f(5, i, 0): # 0 - ничей ход, 1 – Петя, 2 – Ваня, 3 – Петя и тд
        print(i)

