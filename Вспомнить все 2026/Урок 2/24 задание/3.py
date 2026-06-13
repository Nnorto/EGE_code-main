s = open('../file24/test24.txt').readline()

while 'AA' in s or 'BB' in s or 'CC' in s or 'DD' in s or 'EE' in s:
    s = s.replace('AA', 'A A')
    s = s.replace('BB', 'B B')
    s = s.replace('CC', 'C C')
    s = s.replace('DD', 'D D')
    s = s.replace('EE', 'E E')

s = s.split(' ')
print(s)
print(len(max(s, key=len)))
