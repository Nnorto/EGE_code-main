def ss8(n):
    s = 0
    while n > 8:
        s += n % 8
        n //= 8
    s += n
    return s
print(ss8(10))