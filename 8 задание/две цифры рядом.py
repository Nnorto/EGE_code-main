import itertools
c = 0
for x in itertools.product('01234567', repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        if len(set(s)) == 3:
            if (s[0] == s[1]) + (s[1] == s[2]) + (s[2] == s[3]) == 1:
                c += 1
print(c)

from itertools import *
alf="01234567"
index=0
count=0
for x in product(alf,repeat=4):
    s = "".join(x)
    index+=1
    if s[0]!= '0':
        for i in alf:
            if len(set(s))==3 and ((str(i)+str(i)) in s):
                count+=1
print(count)
