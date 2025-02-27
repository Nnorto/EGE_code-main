for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x - 3*y < a) or (y > 400) or (x > 56)) == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag:
        print(a)
        break