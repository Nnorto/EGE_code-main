s = open('../file24/test24.txt').readline()

while 'AA' in s:
    s = s.replace('AA', 'A A')

s = s.split(' ')
print(s)
print(len(max(s, key=len)))


