s = open('../file24/test24.txt').readline()

while 'ACCB' in s:
    s = s.replace('ACCB', 'ACC CCB')

s = s.split(' ')
print(s)
print(len(max(s, key=len)))


