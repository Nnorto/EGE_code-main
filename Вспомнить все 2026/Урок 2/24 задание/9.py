s = open('../file24/test24.txt').readline()

for x in 'MNOP': s = s.replace(x, 'N')
# s = 'NNNNNNNNNNNNNNNNN'
while 'NNN' in s:
    s = s.replace('NNN', 'NN NN')
s = s.split()

print(len(max(s, key=len)))

