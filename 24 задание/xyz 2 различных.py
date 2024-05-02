s = open('24 файл').readline()
kt = 1
m_p = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        kt += 1
        m_p = max(m_p, kt)
    else:
        kt = 1
print(m_p)
