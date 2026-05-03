from re import *
s = open('Файлы/k7a-1.txt').readline()
reg = r'[ABC]+'

print(max([len(x.group()) for x in finditer(reg, s)]))

