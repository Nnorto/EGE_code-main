from string import *

for x in printable[:25]:
    t1 = int(f'11353{x}12', 25)
    t2 = int(f'135{x}21', 25)
    s = t1 + t2
    if s % 24 == 0:
        print(s // 24)