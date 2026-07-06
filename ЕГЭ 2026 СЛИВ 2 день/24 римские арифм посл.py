from re import *
s = open('24.txt').readline()
num = r'(M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))'
reg = rf'(?=({num}([+-]{num})*))'
maxl = max(len(x.group(1)) for x in finditer(reg, s))
print(maxl)