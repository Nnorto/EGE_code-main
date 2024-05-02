alf = 'ЕКМОПРТЬЮ'
index = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    index += 1
                    if s[0] != 'Е' and s.count('К') == 2:
                        print(index)
                        exit()


