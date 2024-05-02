f = open('24 файл')
c = 0
for s in f:
    if s.count('C') > s.count('B'):
        c += 1

print(c)