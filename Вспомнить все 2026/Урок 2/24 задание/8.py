s = open('../file24/24_23osn.txt').readline()

from string import *
alf18 = printable[:18].upper()
for x in printable:
    if x not in alf18:
        s = s.replace(x, ' ')

s = s.split(' ')
print(len(max(s, key=len)), max(s, key=len))

