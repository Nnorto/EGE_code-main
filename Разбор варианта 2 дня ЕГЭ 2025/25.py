def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def f(n):
    lst = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if prime(i):
                lst.append(i)
            if prime(n//i):
                lst.append(n // i)
    return sorted(set(lst))
kp = 0
for i in range(7_000_001, 10**10):
    m = 0
    if len(f(i)) > 0: # сколько делителей надо
        m = min(f(i)) + max(f(i))
        if m % 100 == 13:
            print(i, m)
            kp += 1
            if kp == 5:
                break