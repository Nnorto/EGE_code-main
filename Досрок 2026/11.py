from math import *
x = 289
i = ceil(log2(10 + 1015))
vbyte = ceil(x * i / 8)
print(vbyte * 524288/2**20)