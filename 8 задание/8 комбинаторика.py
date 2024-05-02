alf = 'КУМА'
count = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    if (s[0] == 'К' or s[0] == 'М') and (s[4] == 'У' or s[4] == 'А'):
                        count += 1
print(count)

'''

alf = 'КУМА'
count = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    if s[0] in 'КМ' and s[-1] in 'АУ':
                        count += 1
print(count)

'''
