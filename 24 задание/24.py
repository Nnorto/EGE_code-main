f = open('test.txt')
s = f.readline()
print(len(s))
se = s.split('X')
mk = 0
a = 3
k = 2
for j in range(len(se)-k):
    s = ''.join(se[j:j+k+1])
    print(s)
    if s.count('A') < a:
        continue
    else:
        sp = s.split('A')
        print('\t', sp)
        sm = a + k
        for i in range(0, a+1):
            sm += len(sp[i])
        mk = max(mk, sm)
        for i in range(1, len(sp) - a):
            sm = sm - len(sp[i-1]) + len(sp[i+a])
            mk = max(mk, sm)
        print('\t', '\t', mk, sm)
print(mk)