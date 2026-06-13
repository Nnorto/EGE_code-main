from itertools import *
alf = '0123'
cnt = 0
for x in product(alf, repeat=3):
    s = ''.join(x)
    if int(s[0]) > int(s[1]) > int(s[2]):
        cnt += 1
        print(s)
print(cnt)