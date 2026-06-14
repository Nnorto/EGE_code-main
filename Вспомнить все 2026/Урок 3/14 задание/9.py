for x in range(1, 2025 + 1):
    n = 3**100 - x
    cnt = 0
    while n > 0:
        if n % 3 == 0:
            cnt += 1
        n //= 3
    if cnt == 5:
        print(x)

# 243 - min
# 2024 - max
