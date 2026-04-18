def f(x, y):
    A = 3 <= x <= 60
    B = 177 % x == 0 and x not in [1, 177]
    C = y % x == 0 and x not in [1, y]
    return C <= (A and (not B))

for y in range(1, 3077):
    d = [z for z in range(2, y) if y % z == 0]
    if d and all(f(y, x) for x in range(2, 3077)):
        print(y)