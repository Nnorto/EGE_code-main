alf = "аекптч"
c = 0
res_c = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            s = x1+x2+x3+x4+x5+x6+x7
                            c += 1
                            """
                            if s == 'аптечка' or s == 'печатка':
                                print(c)
                            """
                            if 28921 < c < 154381:
                                res_c += 1

print(res_c)

