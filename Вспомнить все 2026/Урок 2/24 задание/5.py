s = open('../file24/test24.txt').readline()

while 'AD' in s:
    s = s.replace('AD', 'A D')

while 'DA' in s:
    s = s.replace('DA', 'D A')

s = s.split(' ')
print(s)
print(len(max(s, key=len)))


