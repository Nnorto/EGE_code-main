import itertools

a = '012345678'
c = 0
for x in itertools.product(a, repeat=6):
    s = ''.join(x)
    if s[0] != '0':
        if (s[-1] not in '23') and (s[0] not in '1357') and s.count('1') >= 2:
            c += 1
print(c)

a = '012345678'
c = 0
for x1 in '2468':
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in '0145678':
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s.count('1') >= 2:
                            c += 1

print(c)
