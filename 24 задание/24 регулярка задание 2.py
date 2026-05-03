from re import *
s = open('Файлы/24-196.txt').readline()
reg = r'(ZX|ZY)+'

print(max([len(x.group()) // 2 for x in finditer(reg, s)]))

