for n in reversed(range(4, 10000)):
    s = '5'+'2'*n
    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)

    if sum(list(map(int, s))) == 1685:
        print(n)
        break

answ = 4200  # долго считает