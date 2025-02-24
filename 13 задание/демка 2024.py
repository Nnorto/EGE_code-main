from ipaddress import *


net = ip_network('192.168.32.160/255.255.255.240', 0)
count = 0
for ad in net:
    ad2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 2 == 0:
        count += 1
print(count)



from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)
k = 0
for ad in net:
    ad2 = f'{ad:b}'
    # add2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 4 != 0:
        k += 1
print(k)




