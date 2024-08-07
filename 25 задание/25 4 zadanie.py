def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True

def sum_del(n):
    a = []
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            if d * d != n:
                if prime(d):
                    a.append(d)
                if prime(n // d):
                    a.append(n // d)
            else:
                if prime(d):
                    a.append(d)
    return sum(a)

k = 0
for n in range(550_000+1, 10**10):
    s = sum_del(n)
    if s % 10 == 7:
        k += 1
        print(n, s)
        if k == 5:
            break


"""
4) (Аналог сборника Крылова)) Пусть S – сумма различных натуральных делителей целого числа, 
являющихся простыми числами, не считая самого числа.
Напишите программу, которая перебирает целые числа, большие 550 000,
 в порядке возрастания и ищет среди них такие, для которых значение S оканчивается на цифру 7. 
Программа должна найти и вывести первые 5 таких чисел и соответствующие им значения S.
Формат вывода: для каждого из 5 таких найденных чисел 
в отдельной строке сначала выводится само число, затем значение S.
 Строки выводятся в порядке возрастания найденных чисел. Например, для числа 20 S = 2 + 5 = 7.
"""