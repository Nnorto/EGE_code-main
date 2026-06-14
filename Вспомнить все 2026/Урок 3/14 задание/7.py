from string import *
alf = printable[:16]

for x in alf:
    for y in alf:
        t1 = int(f'27a{x}23', 16)
        t2 = int(f'8{y}e5d2', 16)
        s = t1 + t2
        if s % 5 == 0:
            print(int(x, 16) + int(y, 16))