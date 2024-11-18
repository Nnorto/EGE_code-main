from ipaddress import *

 # чем больше маска тем меньше компов в сети может быть
count = 0
for mask in range(16, 25): # x будем искать тут
    net = ip_network('255.220.33.150/' + str(mask), 0)
    for ad in net:
        add = bin(int(ad))[2:].zfill(32)
        adl = add[:16]
        adr = add[16:]
        if adl.count('1') < adr.count('1'):
            break
    else:
        print(mask, net.netmask)

print("или")

for x in range(16, 25):
    net = ip_network(f'255.220.33.150/{x}', 0)
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') < ad_bin[16:].count('1'):
            break
    else:
        print(x, net.netmask)

print("или")

for mask in range(16, 24 + 1):
    # в третем байте может быть 8 "1"
    #значит маску я буду перебирать от 16 до 24 единиц
    # 24 = 16 единиц + 8 единиц
    net = ip_network(f'255.220.33.150/{mask}', 0)
    k = 0
    flag = True
    for ad in net:
        ad2 = bin(int(ad))[2:].zfill(32)
        lev = ad2[:16]
        prav = ad2[16:]
        if lev.count('1') <  prav.count('1'):
            flag = False
            break
    if flag == True:
        print(mask, net.netmask)










