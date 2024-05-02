from ipaddress import *

 # чем больше маска тем меньше компов в сети может быть
count = 0
net = ip_network('15.140.159.230/255.255.252.0', 0)
for ad in net:
    add = bin(int(ad))[2:].zfill(32)
    adl = add[:16]
    adr = add[16:]
    if adl.count('1') >= adr.count('1'):
        count += 1
print(count)






