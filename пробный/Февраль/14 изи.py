def ss49(n):
    s = []
    while n > 0:
        s.append(n%49)
        n //= 49
    return s


num = abs((18 * (7**108)) - (5 * (49**76)) + (343**35) - 50)  # подстава тут отрицательное число :)
s = ss49(num)
print(sum(s))