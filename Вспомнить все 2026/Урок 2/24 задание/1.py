s = open('../file24/test24.txt').readline()

s = s.replace('D', 'E')
s = s.split('E')
print(len(max(s, key=len)))

from re import *
r = r'[ABC]+'
s = open('../file24/test24.txt').readline()
res = [x.group() for x in finditer(r, s)]
print(len(max(res, key=len)))