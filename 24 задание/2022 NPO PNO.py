s = open('24 файл').readline()
s = s.replace('NPO', '*')
s = s.replace('PNO', '*')
maxk = -1
for x in range(100):
    if '*'*x in s:
        maxk = x
print(maxk)