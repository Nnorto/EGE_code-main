from re import *
s = open('Файлы/24_23osn.txt').readline()
num = r'[1-9A-F]+'
m = max([x.group() for x in finditer(num, s)], key=len)
print(len(m))

s = open('Файлы/24_23osn.txt').readline()
for i in range(len(s)):
    if s[i] not in '123456789ABCDEF':
        s = s.replace(s[i], ' ')
s = s.split()
print(len(max(s, key=len)))