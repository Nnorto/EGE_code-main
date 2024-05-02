alf = 'АЛПЦЯ'
index = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    index += 1
                    if s.count('А') <= 1 and s.count('П') == 2 and s.count('Л') == 0:
                        print(index)
                        exit()


