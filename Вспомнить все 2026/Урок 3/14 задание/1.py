n = 6*343**1156 - 5*49**1147 + 4*7**1153 - 875
cnt = 0
while n > 0:
    if n % 7 == 6:
        cnt += 1
    n //= 7

print(cnt)