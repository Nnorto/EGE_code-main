def prime(n):
    """Функция для нахождения простого числа"""
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def proizvdel(n):
    """
    функция для
    нахождения числа которое можно
    представить как произведение двух различных простых делителей
    """
    d = 2
    while d * d <= n:
        if n % d == 0:
            if prime(d) and prime(n // d) and d != n // d:
                return True
        d += 1
    return False


def del3prime(n):
    """
    Функция которое находит число
    которое можно представить как
    произведение 3-х различных простых делителей
    """
    d = 2
    while d * d <= n:
        if n % d == 0:
            if prime(d) and proizvdel(n // d):
                return True
        d += 1
    return False


count = 0
maxn = 0
for n in range(105673, 220784 + 1):
    if del3prime(n):
        count += 1
        maxn = max(maxn, n)
print(count, maxn)
