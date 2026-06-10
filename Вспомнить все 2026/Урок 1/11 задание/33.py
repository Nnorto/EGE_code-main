from math import *

for x in range(1, 1000000):
    alf  = 52 + 10 + 455
    i = ceil(log2(alf))
    b_passw = ceil(x*i / 8)
    if 1200 * b_passw <= 413 * 2**10:
        print(x)
