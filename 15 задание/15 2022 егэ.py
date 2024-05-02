def dell(x, a):
    return x % a == 0


for a in range(1, 100):
    count = 0
    for x in range(1, 1000):
        if (dell(x, 2)) <= (not(dell(x, 3))) or (x + a >= 90):
            count += 1
        if count == 999:
            print(a)
