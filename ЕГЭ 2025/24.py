f = open('24.txt')
s = f.readline()
s = s.replace('D', ' D')
for x in '1234567890':
    s = s.replace(x, '1')
s = s.split()
maxd = 0
for el in s:
    if el[0] == "D" and el.count('1') == 50:
        maxd = max(maxd, len(el))
print(maxd)


