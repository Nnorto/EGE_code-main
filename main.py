from itertools import product
count = 0
alf = '012345678'
for x in product(alf, alf, alf, alf, alf):
    s = ''.join(x)
    if s[0] != '0':
        s = s.replace('2', '*').\
            replace('3', '*').\
            replace('4', '*').\
            replace('5', '*')
        if s.count('6') == 1 and '*6' not in s and '6*' not in s:
            count += 1
print(count)