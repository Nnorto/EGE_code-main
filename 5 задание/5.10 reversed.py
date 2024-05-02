for n in range(100):
    n2 = bin(n)[2::]
    n2 = n2[::-1]
    r = int(n2, 2)  # функция int сама отбрасывает незначащие нули
    if r == 9:
        print(n)

