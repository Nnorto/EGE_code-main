from re import *
s = open('СборникЕГЭ_2024_задание24_3.txt').readline()
s = s.replace('*', 'Z')
s = s.replace('+', 'Z')
num = r'(0|[1-9][0-9]*)'
reg = rf'{num}(Z{num})*'
print(max([len(x.group()) for x in finditer(reg, s)]))

from re import *
s = open('СборникЕГЭ_2024_задание24_3.txt').readline()
num = r'(0|[1-9][0-9]*)'
proizv = rf'(({num}\*)*0(\*{num})*)'
reg = rf'{proizv}(\+{proizv})+'
reg = rf'(?=({reg}))'
print(len(max([x.group(1) for x in finditer(reg, s)], key=len)))
