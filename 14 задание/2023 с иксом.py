for x in range(19):
    s = (int('76079645', 19) + x * 19 ** 7) + (int('35042', 19) + x * 19 ** 4) + (int('33206', 19) + x * 19 ** 3)
    if s % 18 == 0:
        print(s // 18)
        break