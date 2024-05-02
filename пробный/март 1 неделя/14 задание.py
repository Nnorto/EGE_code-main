"""
14y5x2 +31x2y3
14 основание
"""

max_sum = -1
a = []
for x in range(14):
    for y in range(14):
        t1 = int('140502', 14) + y * 14**3 + x * 14
        t2 = int('310203', 14) + x * 14**3 + y * 14
        s = t1 + t2
        if s % 9 == 0:
            max_sum = max(max_sum, s)
            a.append([s, x, y])

"""print(a) # [2399913, 11, 9], [2399913, 12, 8], [2399913, 13, 7]"""

print(max_sum//9)
