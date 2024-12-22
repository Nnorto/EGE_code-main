from itertools import product
alf = '01'
c = 0
for x in product(alf, repeat=11):
    s = ''.join(x)
    if (8 + s.count('1')) % 5 != 0:
        c += 1

print(c)