from itertools import *
alf = 'авнрья'
ns = 0
for x in product(alf, repeat=5):
    ns += 1
    s = ''.join(x)
    if s[0] != "я" and s.count('ь') <= 1 and "яя" not in s:
        print(ns, s)