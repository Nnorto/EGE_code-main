from string import *
alf = printable[:26]

for x in alf:
    if all((int(f'13{y}{x}5', 26) + int(f'34{y}13', 26)) % 8 == 0 for y in alf):
        print((int(f'13{3}{x}5', 26) + int(f'34{3}13', 26)) // 8)
        break

from string import *
alf = printable[:26]

for x in alf:
    cnt = 0
    for y in alf:
        t1 = int(f'13{y}{x}5', 26)
        t2 = int(f'34{y}13', 26)
        s = t1 + t2
        if s % 8 == 0:
            cnt += 1
    if cnt == 26:
        t1 = int(f'13{3}{x}5', 26)
        t2 = int(f'34{3}13', 26)
        s = t1 + t2
        print(s // 8)
        break

from string import *
alf = printable[:26]

for x in alf:
    flag = 1
    for y in alf:
        t1 = int(f'13{y}{x}5', 26)
        t2 = int(f'34{y}13', 26)
        s = t1 + t2
        if not(s % 8 == 0):
            flag = 0
    if flag:
        t1 = int(f'13{3}{x}5', 26)
        t2 = int(f'34{3}13', 26)
        s = t1 + t2
        print(s // 8)
        break


from string import *
alf = printable[:26]

for x in alf:
    for y in alf:
        t1 = int(f'13{y}{x}5', 26)
        t2 = int(f'34{y}13', 26)
        s = t1 + t2
        if not(s % 8 == 0):
            break
    else:
        t1 = int(f'13{3}{x}5', 26)
        t2 = int(f'34{3}13', 26)
        s = t1 + t2
        print(s // 8)
        break