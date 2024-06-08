def dell(x, a):
    return x % a == 0

for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        if ((dell(x, 2) <= (not (dell(x, 5)))) or (x + a >= 70)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

for a in range(1, 500):
    for x in range(1, 500):
        if ((dell(x, 2) <= (not (dell(x, 5)))) or (x + a >= 70)) == 0:

            break
    else:
        print(a)
        break

def al(x, a):
    return (dell(x, 2) <= (not (dell(x, 5)))) or (x + a >= 70)
for a in range(1, 500):
    if all(al(x, a) for x in range(1, 500)):
        print(a)
        break
