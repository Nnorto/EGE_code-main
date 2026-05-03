from re import *
s = open('Файлы/24-212.txt').readline()
reg = r'([BCD][AO])+'

print(max([len(x.group()) // 2 for x in finditer(reg, s)]))

