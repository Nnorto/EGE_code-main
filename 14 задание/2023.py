import string
for x in range(19):
    n1 = 9 * 19**7 + 8 * 19 ** 6 + x * 19 ** 5 + 7 * 19 ** 4 + 9 * 19 ** 3 + 7 * 19 ** 2 + 3 * 19 + 1
    n2 = 3 * 19 ** 4 + 6 * 19 ** 3 + x * 19 ** 2 + 1 * 19 + 4
    s = n1 + n2
    if s % 18 == 0:
        print(s // 18)
        break


buk = 'qwertyuiopasdfghjklzxcvbnm'.upper()
buk = sorted(buk)
s = ''
for i in range(len(buk)):
    s += buk[i]


alf2 = string.ascii_uppercase
alf = "0123456789" +alf2[:9]

for x in alf:
    t1 = int('98' + x + '79731', 19)
    t2 = int('36' + x + '14', 19)
    r = t2 + t1
    if r % 18 == 0:
        print(r // 18)
        break

for x in range(19):
    t1 = int('98' + '0' + '79731', 19) + x * 19**5
    t2 = int('36' + '0' + '14', 19) + x * 19**2
    r = t2 + t1
    if r % 18 == 0:
        print(r // 18)
        break
