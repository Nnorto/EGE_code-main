import string
alf = string.ascii_uppercase
ss = '0123456789' + alf[:16]
for x in ss:
    for y in ss:
        t1 = int(f'13{y}{x}5', 26)
        t2 = int(f'24{y}13', 26)
        s = t1 + t2
        if s % 8 != 0:
            break
    else:
        t1 = int(f'132{x}5', 26)
        t2 = int(f'24213', 26)
        s = t1 + t2
        print(x, s // 8)
        break

for x in ss:
    flag = True
    for y in ss:
        t1 = int(f'13{y}{x}5', 26)
        t2 = int(f'24{y}13', 26)
        s = t1 + t2
        if s % 8 != 0:
            flag = False

    if flag == True:

        t1 = int(f'132{x}5', 26)
        t2 = int(f'24213', 26)
        s = t1 + t2
        print(x, s // 8)
        break

def f(x, y):
    t1 = int(f'13{y}{x}5', 26)
    t2 = int(f'24{y}13', 26)
    s = t1 + t2
    return s

for x in ss:
    if all(f(x, y) % 8 == 0 for y in ss):
        t1 = int(f'132{x}5', 26)
        t2 = int(f'24213', 26)
        s = t1 + t2
        print(x, s // 8)
        break


for x in range(26):
    for y in range(26):
        t1 = int('13005', 26) + x * 26 ** 1 + y * 26 ** 2
        t2 = int('24013', 26) + y * 26 ** 2
        s = t1 + t2
        if s % 8 != 0:
            break
    else:
        t1 = int(f'13205', 26) + x * 26 ** 1
        t2 = int(f'24213', 26)
        s = t1 + t2
        print(x, s // 8)
        break


