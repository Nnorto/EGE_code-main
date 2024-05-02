n = 9**70 + 3**210 - 8
s = ''
while n > 0:
    s = str(n % 3) + s
    n //= 3
print(sum(list(map(int, s))))