from math import *

for alf in range(1, 10000):
    i = ceil(log2(alf))
    b_passw = ceil(345*i / 8)
    if 909 * b_passw > 447 * 2**10:
        print(alf)
        break
