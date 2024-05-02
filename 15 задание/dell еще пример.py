def dell(x, a):
    return x % a == 0


for a in range(1, 50):
    count = 0
    for x in range(1, 10000):
        if dell(x, a) or (not dell(x, 10)) or (not dell(x, 12)):
            count += 1
        if count >= 9999:
            print(a)
