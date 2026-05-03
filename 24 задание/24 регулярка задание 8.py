from re import *
s = open('Файлы/24-310.txt').readline()

num = r'(0|[12][012]*)'
reg = rf'{num}([*+]{num})+'
m = max([x.group() for x in finditer(reg, s)], key=len)
print(m)
print(len(m))