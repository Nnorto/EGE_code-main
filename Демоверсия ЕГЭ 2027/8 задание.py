from itertools import *
alf = sorted('акцент')
p_num = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    p_num += 1
    if p_num % 2 == 0:
        if s[0] not in 'аек':
            if s.count('т') >= 1:
                print(p_num, s)
                break

