from math import *

for alf in range(1, 1000):
    i = ceil(log2(alf))
    sr = ceil(65 * i / 8) # вес сер номера в БАЙТАХ
    if 131_072 * sr < 9 * 2**20:
        print(alf)

# 256