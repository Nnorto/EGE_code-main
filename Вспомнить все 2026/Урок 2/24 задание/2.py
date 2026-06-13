s = open('../file24/test24.txt').readline()

s = s.split('A')
print(len(max(s, key=len)))

from re import *
s = open('../file24/test24.txt').readline()
reg = r'[^A]+'
# reg = r'[BCDE]+'
res = [x.group() for x in finditer(reg, s)]
print(len(max(res, key=len)))