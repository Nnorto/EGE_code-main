from re import *
f = open('Файлы/24_19968.txt')
num = r'([1-5][0-5]*|0)'
reg = rf'{num}([+*]{num})+'
reg = rf'(?=({reg}))'
s = f.readline()
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(m)
print(len(m))