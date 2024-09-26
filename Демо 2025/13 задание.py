from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', 1)
c = 0
for ad in net:
    ad2 = bin(int(ad))[2:]
    if ad2.count('1') % 5 != 0:
        c += 1

print(c, net.num_addresses)
