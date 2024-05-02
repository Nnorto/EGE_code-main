from ipaddress import *

 # чем больше маска тем меньше компов в сети может быть
count = 0
for A in reversed(range(256)): # A будем искать тут reversed потому что просят максимальный
    net = ip_network(f'227.31.{A}.139/255.255.255.224', 0)
    flag = True
    for ad in net:
        add = bin(int(ad))[2:].zfill(32)
        adr = add[:16]
        adl = add[16:]
        if adr.count('0') > adl.count('0'):
            flag = False
            break
    if flag == True:
        print(A)
        break
