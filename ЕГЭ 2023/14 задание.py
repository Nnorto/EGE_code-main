for x in range(19):
    t1 = int('98079731', 19) + x * 19 ** 5
    t2 = int('36014', 19) + x * 19 ** 2
    s = t1 + t2
    if s % 18 == 0:
        print(s//18)
        break

# ИЛИ
for x in range(19):
    t1 = 9 * 19**7 + 8 * 19**6 + x * 19**5 + 7 * 19**4 + 9 * 19**3 + 7 * 19**2 + 3 * 19**1 + 1
    t2 = 3 * 19**4 + 6 * 19**3 + x * 19**2 + 1 * 19**1 + 4
    s = t1 + t2
    if s % 18 == 0:
        print(s//18)
        break

# ИЛИ
import string
letters = string.ascii_uppercase[:9]
alf = '0123456789' + letters
for x in alf:
    t1 = int('98' + x + '79731', 19)  # или  t1 = int(f'98{x}79731', 19)
    t2 = int('36' + x + '14', 19)  # или  t2 = int(f'36{x}14', 19)
    s = t1 + t2
    if s % 18 == 0:
        print(s//18)
        break


