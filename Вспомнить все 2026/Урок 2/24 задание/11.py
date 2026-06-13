f = open('../file24/24-s1.txt')

k = 0
for s in f:
    if s.count('C') > s.count('B'):
        k += 1
print(k)