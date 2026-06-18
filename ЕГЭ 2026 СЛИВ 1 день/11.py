from math import *
for alf in range(1, 1000):
    i = ceil(log2(alf))
    sr = ceil(65*i/8) # в байтах
    if 131072*sr <= 9 * 2**20:
        print(alf)


from math import *
for x in range(1, 1000):
    alf = 10 + 26 + 34
    i = ceil(log2(alf))
    sr = ceil(x*i/8) # в байтах
    if 1142*sr > 305*2**10:
        print(x)
        break