s = open('24 файл').readline()

a = s.split('D')

print(len(max(a, key=len)))

# длинный способ

s = open('24 файл').readline()
kt = 0
m_p = 0
for i in s:
    if i != 'D':
        kt += 1
        m_p = max(m_p, kt)
    else:
        kt = 0
print(m_p)
