from string import *
alf = ascii_uppercase
f = open('24_22449.txt')
s = f.readline()
lim = 500_000
ifs = 0
ts = 0
for i in range(lim):
    ts += alf.index(s[i]) + 1
maxts = ts

for i in range(lim, len(s)):
    ts += -(alf.index(s[i - lim]) + 1) + (alf.index(s[i]) + 1)
    if ts > maxts:
        maxts = ts
        ifs = i - (lim - 1)
print(ifs)