from ipaddress import *

 # чем больше маска тем меньше компов в сети может быть
for A in range(16, 25): # A будем искать тут reversed потому что просят максимальный
    net = ip_network(f'117.157.2.8/{A}', 0)
    flag = True
    for ad in net:
        add = bin(int(ad))[2:].zfill(32)
        adr = add[:16]
        adl = add[16:]
        if adr.count('1') < adl.count('1'):
            flag = False
            break

    if flag:
        print(A)
        break


