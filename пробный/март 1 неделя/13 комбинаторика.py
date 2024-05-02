from itertools import *
alf = '01'
count = 0
for i in product(alf, repeat=5):
    s = ''.join(i)
    if '111' not in s:
        if '000' not in s:
            if s[0] != '1':
                print(s)
                count += 1
print(count)