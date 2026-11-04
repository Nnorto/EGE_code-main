from math import *
for alf in range(1, 1000):
    i = ceil(log2(alf))
    sr = ceil(157 * i/8)
    if sr * 12450 <= 955 * 2**10:
        print(alf)