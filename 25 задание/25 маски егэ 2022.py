if 12367 % 123 == 0:
    print(12367, 12367 // 123)

for n in range(10):
    x = "123" + str(n) + "67"
    x = int(x)
    if x % 123 == 0:
        print(x, x // 123)

for n in range(10):
    for k in range(10):
        x = "123" + str(n) + str(k) + "67"
        x = int(x)
        if x % 123 == 0:
            print(x, x // 123)

for n in range(10):
    for k in range(10):
        for m in range(10):
            x = "123" + str(n) + str(k) + str(m) + "67"
            x = int(x)
            if x % 123 == 0:
                print(x, x // 123)

