from re import *
s = open('Файлы/СборникЕГЭ_2024_задание24_3.txt').readline()

num = r'([1-9][0-9]*|0)'
proizv = rf'(({num}\*)*0(\*{num})*)'
reg = rf'{proizv}(\+{proizv})+'
reg = rf'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m))