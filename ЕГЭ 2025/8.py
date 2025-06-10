from itertools import *
alf = 'вдёжиноря'
pn = 0
for x in product(alf, repeat=5):
    pn += 1
    s = ''.join(x) # получаем строку
    if pn % 2 == 0:
        if s[0] not in 'яждё':  # слово не начинается на опр букву
            if s.count('ё') == 1:
                print(pn)