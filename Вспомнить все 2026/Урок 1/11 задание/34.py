from math import *

for alf in range(1, 1000000):
    i = ceil(log2(alf))
    b_passw = ceil(420*i / 8)
    if 977 * b_passw <= 376 * 2**10:
        print(alf)
