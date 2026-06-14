from string import *
alf = printable[:23]
for x in alf:
    t1 = int(f'7{x}38596', 23)
    t2 = int(f'14{x}36', 23)
    t3 = int(f'61{x}7', 23)
    s = t1 + t2 + t3
    if s % 22 == 0:
        print(s // 22)