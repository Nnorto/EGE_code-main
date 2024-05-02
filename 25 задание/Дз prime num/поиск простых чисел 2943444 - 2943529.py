def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


p_num = 0  # порядковый номер числа в последовательности
for x in range(2943444, 2943529 + 1):
    if prime(x):
        p_num += 1
        print(p_num, x)


"""
1 2943467
2 2943491
3 2943503
4 2943527
"""