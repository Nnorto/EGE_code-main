from re import *
s = open('Файлы/24-204.txt').readline()
reg = r'(AA|CC)+'
reg = rf'(?=({reg}))'
for x in finditer(reg, s):
    print(x.group(1))
    input()
# print(max([len(x.group(1)) for x in finditer(reg, s)]))

