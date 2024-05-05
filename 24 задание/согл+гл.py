f = open('24 файл')
s = f.readline()
k = 0
maxk = 0
sogl = 'BCD'
gl = 'AU'
i = 0
while i < len(s) - 1:
    if s[i] in sogl and s[i + 1] in gl:
        k += 1
        i += 2
        maxk = max(maxk, k)
    else:
        k = 0
        i += 1
print(maxk)

f = open('24 файл')
s = f.readline()
s = s.replace('U', 'A')
s = s.replace('D', 'B')
s = s.replace('C', 'B')
s = s.replace('BA', '*')
s = s.replace('A', '1')
s = s.replace('B', '1')
print(s)
s = s.split('1')
print(s)

maxs = 0
for i in range(len(s)):
    maxs = max(maxs, len(s[i]))

print(maxs)

print(len(max(s, key=len)))
s = open('24 файл').readline()
s = s.replace('U', 'A')
s = s.replace('C', 'B')
s = s.replace('D', 'B')
s = s.replace('BA', '*')
maxk = -1
for x in range(100):
    if '*'*x in s:
        maxk = x
print(maxk)





