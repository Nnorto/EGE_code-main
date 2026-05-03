from re import *
s = open('Файлы/24-298.txt').readline()

num = r'[1-9][0-9]*'
reg = rf'{num}([-*]{num})+'
reg = rf'(?=({reg}))' # пишем всегда, чтобы учесть пересечения
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m))
print(m)