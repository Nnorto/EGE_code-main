from re import *
s = open('Файлы/24-239.txt').readline()
reg = r'(YZZ|YZ|XY)+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))

