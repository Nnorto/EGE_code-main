"""
Сколько цифр 0 содержится в этой записи?
"""
def f(n):
    x = 216**5 + 6**3 - 1 - n

    s = ""

    while x > 0:
        s += str(x % 6)
        x //= 6
    return s.count("5")


for x in range(1000):
    if f(x) == 12:
        print(x)
        break