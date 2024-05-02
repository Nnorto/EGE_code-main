def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True

def del_2(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            if prime(d) and prime(n // d):
                return True
        d += 1
    return False

max_num = -1
count = 0
for x in range(125697, 190234 + 1):
    if del_2(x):
        count += 1
        max_num = max(max_num, x)

print(count, max_num)

answ = "14047 190231"