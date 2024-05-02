from itertools import *

count = 0
for x in product("0123456789", repeat=6):
    s = ''.join(x)
    if int(s) % 5 == 0 and len(set(s)) == len(s) and s[0] != '0':
        s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        s = s.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        if '11' not in s and '22' not in s:
            count += 1

print(count)


#или

alf = '0123456789'
c = 0
for x in permutations(alf, 6):
    s = ''.join(x)
    if s[0] != '0' and int(s) % 5 == 0:
        s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        s = s.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        if '11' not in s and '22' not in s:
            c += 1
print(c)