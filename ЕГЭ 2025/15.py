def f(x, y, a):
    return (y + 2*x < a) or (x > 20) or (y > 20)

for a in range(1, 1000):
    if all(f(x,y, a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break