from string import *
alf = printable[:27]
for x in alf:
    t1 = int(f'123{x}24', 27)
    t2 = int(f'135{x}78', 27)
    s = t1 + t2
    if s % 26 == 0:
        print(s // 26)


for x in range(27):
    t1 = int('123024', 27) + x * 27**2
    t2 = int('135078', 27) + x * 27**2
    s = t1 + t2
    if s % 26 == 0:
        print(s // 26)