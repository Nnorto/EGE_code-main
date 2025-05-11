n = 5**20 + 5**10 - 5**13 - 5**3
s = 0
while n > 0:
    s += n % 5
    n //= 5
print(s)
