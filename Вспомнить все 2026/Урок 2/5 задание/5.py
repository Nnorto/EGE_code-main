for n in range(1, 1000):
    n2 = f'{n:b}'
    ns = ''
    for x in n2:
        ns += x*2
    r = int(ns, 2)
    if r > 63:
        print(r)
        break