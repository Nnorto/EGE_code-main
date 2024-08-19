for n in range(4, 10000):
    s = '4' + '8' * n
    while '48' in s or '288' in s or '8888' in s:
        if '48' in s:
            s = s.replace('48', '8', 1)
        if '288' in s:
            s = s.replace('288', '84', 1)
        if '8888' in s:
            s = s.replace('8888', '2', 1)
    summ = sum(list(map(int, s)))
    # или
    summa = s.count('4') * 4 + s.count('2') * 2 + s.count('8') * 8
    if summa == 64:
        print(n)
        break