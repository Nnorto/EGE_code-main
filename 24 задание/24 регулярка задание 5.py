from re import *
s = open('Файлы/24-215.txt').readline()
reg = r'([123][ABC][123])+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) // 3 for x in finditer(reg, s)]))

