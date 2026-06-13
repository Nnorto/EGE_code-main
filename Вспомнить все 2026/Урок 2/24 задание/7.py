s = open('../file24/24_22dosr.txt').readline()

s = s.replace('AB', '*')
s = s.replace('CB', '*')
s = s.replace('A', ' ')
s = s.replace('B', ' ')
s = s.replace('C', ' ')
s = s.split(' ')
print(s[:10])
print(len(max(s, key=len)))


