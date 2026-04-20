print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and (not z) and (not w)) or (x and (not z) and y)
                if f:
                    print(x, y, z, w)
