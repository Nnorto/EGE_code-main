s = open('24 файл').read()
count = 0
s = s.replace('A', 'B')
s = s.replace('C', 'B')
s = s.replace('BB', 'B B')
s = s.replace('BB', 'B B')
s = s.split(" ")
print(len(max(s, key=len)), s)
