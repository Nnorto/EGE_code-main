x = 2 * 216**8 + 4 * 36**12 + 6**15 - 1296

s = ""

while x > 0:
    s += str(x % 6)
    x //= 6

print(s.count("0"))