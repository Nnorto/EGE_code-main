from math import ceil
for x in range(1000, 0, -1):
    s_n = x * 11
    s_nb = ceil(s_n/8)
    more = s_nb * 2000/1024
    if more <= 693:
        print(x)
        break
