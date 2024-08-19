from itertools import *

alf = '0234567'  # исключаем 1
count = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if len(s) == len(set(s)):  # тип все цифры различны (нет повторений)
            s = s.replace('5', '3').replace('7', '3')
            s = s.replace('4', '2').replace('6', '2').replace('0', '2')
            if ('22' not in s) and ('33' not in s):
                count += 1

print(count)

alf = '0234567'  # исключаем 1
count = 0
for x in permutations(alf, r=5):  # тут цифры не повторяются
    s = ''.join(x)
    if s[0] != '0':
        s = s.replace('5', '3').replace('7', '3')
        s = s.replace('4', '2').replace('6', '2').replace('0', '2')
        if ('22' not in s) and ('33' not in s):
            count += 1

print(count)

alf = '0234567'  # исключаем 1
count = 0

for x1 in '234567':  # тут число на 0 не начинается
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    if len(s) == len(set(s)):  # тип все цифры различны (нет повторений)
                        s = s.replace('5', '3').replace('7', '3')
                        s = s.replace('4', '2').replace('6', '2').replace('0', '2')
                        if ('22' not in s) and ('33' not in s):
                            count += 1
print(count)