s = 'ab' * 403
while 'aaa' in s or 'bbb' in s or 'ab' in s:
    s = s.replace('aaa', 'bc', 1)
    s = s.replace('bbb', 'da', 1)
    s = s.replace('ab', 'ba', 1)
    s = s.replace('cd', 'bba', 1)

m = []
m.append(s.count('a'))
m.append(s.count('b'))
m.append(s.count('c'))
m.append(s.count('d'))
i = m.index(max(m))
print(chr(i + ord("A")), max(m))