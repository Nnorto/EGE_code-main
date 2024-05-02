def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True

def del_2(n):
    d = 2
    m = []
    while d * d < n:
        if n % d == 0:
            if prime(d) and prime(n // d):
                m.append(d)
                m.append(n//d)
        d += 1
    return m


min_raz = 10**10  # для поиска минимальной разности
m_res = []  # массив результата, там будет 2 числа
for x in range(523456, 578925 + 1):
    mas = del_2(x)  # массив произведения делителей
    if len(mas) > 0:  # нужно понимать что число может и не быть произведением простых чисел
        raz = abs(mas[0] - mas[1]) # разница = абсолютная разность между 2 элементами массива :)
        if min_raz > raz:
            min_raz = raz
            m_res = mas
print(*m_res)  # ну и ответ, GG SOLO

answ = '739 743'
