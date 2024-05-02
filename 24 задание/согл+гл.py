s = open('24 файл').readline()
s = s.replace('U', 'A')
s = s.replace('C', 'B')
s = s.replace('D', 'B')
s = s.replace('BA', '*')
maxk = -1
for x in range(100):
    if '*'*x in s:
        maxk = x
print(maxk)





