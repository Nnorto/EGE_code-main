def prime_while(n):
    # запомни 1 это не простое число (поэтому это нужно обработать)
    if n > 1:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True
    return False

def prime_for(n):
    # запомни 1 это не простое число (поэтому это нужно обработать)
    if n > 1:
        for d in range(2, int(n**0.5) +1):
            if n % d == 0:
                return False
        return True
    return False

def prime_any(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) +1))

print(prime_any(11), prime_for(11), prime_while(11))