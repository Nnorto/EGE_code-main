s = open('24 файл').readline()
s = s.replace('A', 'C')
s = s.replace('B', 'C')
s = s.replace('D', 'E')

a = s.split('E')

print(len(max(a, key=len)))

# длинный способ

s = open('24 файл').readline()
kt = 0
m_p = 0
for i in s:
    if i == 'A' or i == 'B' or i == 'C':
        kt += 1
        m_p = max(m_p, kt)
    else:
        kt = 0
print(m_p)
