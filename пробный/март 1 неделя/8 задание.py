alf = "ГИПЕРБОЛА"
gl = "ИЕОА"
sgl = 'ГПРБЛ'
count = 0
k = 0
for b1 in alf:
    for b2 in alf:
        for b3 in alf:
            for b4 in alf:
                for b5 in alf:
                    for b6 in alf:
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        k += 1
                        if s[0] in gl or s[5] in gl:
                            count += 1
                        if s[0] not in "ИЕОА" and s[-1] not in "ИЕОА":
                            if (s[1] in gl and s[2] in sgl) \
                                    or (s[2] in gl and s[1] in sgl and s[3] in sgl) \
                                    or (s[3] in gl and s[2] in sgl and s[4] in sgl) \
                                    or (s[4] in gl and s[3] in sgl):
                                count += 1

print(k - count)
