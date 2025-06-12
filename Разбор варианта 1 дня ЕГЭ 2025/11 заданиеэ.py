from math import *

for alf in range(1, 10000):
    i = ceil(log2(alf))
    sr_byte = ceil(172 * i / 8)
    if sr_byte * 356948 >= 54*2**20:
        print(alf)
        break