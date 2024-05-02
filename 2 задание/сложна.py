def f1(x, y, z, w):
    return (w <= y) == (z <= x)


def f2(x, y, z, w):
    return (w <= y) and (not x == z)


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f1(x, y, z, w) == 1 and f2(x, y, z, w) == 0:
                    print(x, y, z, w)