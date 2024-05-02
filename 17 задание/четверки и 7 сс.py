def ss7(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s


f = open('17 файлы/17_22.txt')
a = list(map(int, f))
count = 0
min_r = 1212120120120120
for i in range(len(a) - 3):
    if (abs(a[i]) % 10 == 3)\
            + (abs(a[i+1]) % 10 == 3)\
            + (abs(a[i+2]) % 10 == 3)\
            + (abs(a[i+3]) % 10 == 3) >= 1:
        if (ss7(abs(a[i]))[-1] == '3')\
                + (ss7(abs(a[i+1]))[-1] == '3')\
                + (ss7(abs(a[i+2]))[-1] == '3')\
                + (ss7(abs(a[i]+3))[-1] == '3') == 0:
            count += 1
            ch4 = [a[i], a[i+1], a[i+2], a[i+3]]
            max4 = max(ch4)
            min4 = min(ch4)
            raz = max4 - min4
            min_r = min(min_r, raz)

print(count, min_r)

