from math import *
for alf in range(1, 1000):
    i = ceil(log2(alf))
    kod = ceil(450*i/8) # в байтах
    if 780100*kod <= 83 * 2 ** 20:
        print(alf)