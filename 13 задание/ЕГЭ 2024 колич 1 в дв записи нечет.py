from ipaddress import *
net = ip_network('106.184.0.0/255.248.0.0', 0)
c = 0
for ad in net:
    dv = bin(int(ad))[2:]
    if dv.count('1') % 2 != 0:
        c += 1
print(c, net.num_addresses//2)