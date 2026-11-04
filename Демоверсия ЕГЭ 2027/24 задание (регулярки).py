from re import *
s = open('demo_24.txt').readline()
s = s.replace('6', '1')
s = s.replace('7', '2')
s = s.replace('8', '3')
s = s.replace('9', '4')
num = r'(0|[1-4][0-4]*)'
arifm = rf'(({num})((\-|\*)({num}))*)'
res = []
for x in finditer(arifm, s):
    res.append(len(x.group()))
print(max(res))
