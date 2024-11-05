big = 0
k = int(input())
for x in range(k):
    num = int(input())
    len_n = 0
    n = num
    t_num_posl = num
    while n > 0:
        num = n % 10
        len_n += 1
        n //= 10
    big = big * 10 ** len_n + t_num_posl
    big *= 10

max_el = -10**10
big2 = big
while big > 0:
    num = big % 10
    if num > max_el:
        max_el = num
    big //= 10

count = 0
while big2 > 0:
    num = big2 % 10
    if num == max_el:
        count += 1
    big2 //= 10

print(count)