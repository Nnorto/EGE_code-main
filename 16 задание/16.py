from functools import *
@lru_cache(100)
def f(n):
    if n < 10:
        return 1
    return (n + 3) * f(n - 3)
a, b, c = 0, 0, 0
for i in range(247_600):
    if i == 247_563:
        a = f(i)
    elif i == 247_560:
        b = f(i)
    elif i == 247557:
        c = f(i)
    else:
        f(i)
# print((f(247_563) // 519 - 477 * f(247_560))// f(15))
print((a // 519 - 477 * b)// c)
