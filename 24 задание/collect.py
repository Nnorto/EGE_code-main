import string
import collections
s = open("24 файл").read()
mk = 0
a = []
for i in range(len(s) - 2):
   if s[i] == s[i + 1]:
      a.append(s[i + 2])

alf = string.ascii_uppercase

print(collections.Counter(a))

for x in alf:
   if a.count(x) > mk:
      mk = a.count(x)
      res = x

print(res, mk)

