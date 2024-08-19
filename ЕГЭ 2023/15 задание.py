for a in range(500):
    flag = True
    for x in range(500):
        for y in range(500):
            if ((x + 2*y < a) or (y > x) or (x > 32)) == 0:
                flag = False
                break
    if flag:
        print(a)
        break

# или

for a in range(500):
    if all((x + 2*y < a) or (y > x) or (x > 32) for x in range(500) for y in range(500)):
        print(a)
        break