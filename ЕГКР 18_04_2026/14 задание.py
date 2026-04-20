from string import *

for x in printable[:23]:
    t1 = int(f'761{x}035', 23)
    t2 = int(f'338{x}932', 23)
    s = t1 + t2
    if s % 22 == 0:
        print(s // 22)
        break
        
# 70045642