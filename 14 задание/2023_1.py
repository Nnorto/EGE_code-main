for x in range(22):
    n1 = int('98079641', 22) + x * 22 ** 5
    n2 = int('25043', 22) + x * 22 ** 2
    n3 = int('6305', 22) + x * 22
    s = n1 + n2 + n3
    if s % 21 == 0:
        print(s // 21)
        break