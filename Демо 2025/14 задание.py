for x in range(2030, -1, -1):
    a = 7 ** 170 + 7 ** 100 - x
    s = ''
    while a > 0:
        s = str(a % 7) + s
        a //= 7
    if s.count('0') == 71:
        print(x)
        break
