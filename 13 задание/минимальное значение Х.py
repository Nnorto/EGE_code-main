from ipaddress import *

 # чем больше маска тем меньше компов в сети может быть
count = 0
for mask in range(16, 25): # x будем искать тут
    net = ip_network('255.220.33.150/' + str(mask), 0)
    for ad in net:
        add = bin(int(ad))[2:].zfill(32)
        adr = add[:16]
        adl = add[16:]
        if adr.count('1') < adl.count('1'):
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










