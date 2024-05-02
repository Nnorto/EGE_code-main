def f(num, sist):
    res = ""
    while num > 0:
        res = str(num % sist) + res
        num //= sist
    return res


print(f(13212, 7))
