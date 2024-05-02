import string

s = open('24 файл').readline()
a = []
for i in range(len(a) - 1):
    if s[i] == 'E':
        a.append(s[i + 1])

alf = string.ascii_uppercase
maxk = 0
res = 0
for x in alf:
    if a.count(x) > maxk:
        maxk = a.count(x)
        res = x

print(res, maxk)

a = open('24 файл').readline()
res = 0
s = [0]*26
for i in range(len(a)):
    if a[i] == 'E':
        index = ord(a[i + 1]) - ord('A')
        s[index] += 1
maxk = 0
for i in range(len(s)):
    if s[i] > maxk:
        maxk = s[i]
        res = chr(i + ord('A'))

print(res, maxk)

a = open('24 файл').readline()
res = 0
s = [0]*26
for i in range(len(a)):
    if a[i] == 'E':
        index = ord(a[i + 1]) - ord('A')
        s[index] += 1
maxk = 0
for k,i in enumerate(s):
    if i > maxk:
        maxk = i
        res = chr(k + ord('A'))

print(res, maxk)