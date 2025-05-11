from string import *
for x in printable[:21]:
    if all((int(f'12{y}{x}9',21) + int(f'36{y}99',21)) % 18 == 0 for y in printable[:21]):
        t1 = int(f'125{x}9',21)
        t2 = int(f'36599',21)
        s = t1 + t2
        print(s//18)
        break