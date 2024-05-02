def prime(number):
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        else:
            d += 1
    return True


for n in range(0, 10000):

    s = '>' + '1' * 10 + '2' * n + '3' * 10
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>1', 1)

    su = s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3
    if prime(su):
        print(n, su)
        break
