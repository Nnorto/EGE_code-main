from math import *

for x in range(1, 10000):
    alf = 100 + 10
    i = ceil(log2(alf))
    passw = x * i
    b_passw = ceil(x*i / 8)
    if 100 * b_passw > 110 * 2**10:
        print(x)
        break