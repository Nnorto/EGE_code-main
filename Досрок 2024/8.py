from itertools import *

f_count = 1
for x in product("АПРСУ", repeat=5):
    f = ''.join(x)
    if not(f.count('У') <= 1 and 'АА'not in f):
        f_count += 1
    else:
        break

print(f_count)

alf = "апрсу"
index = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1+x2+x3+x4+x5
                    index += 1
                    if "аа" not in s:
                        if s.count("у") <= 1:
                            print(s, index)
                            exit()