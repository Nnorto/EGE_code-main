from ipaddress import *
net = ip_network('206.158.124.67/255.255.224.0', 0)
k = -1
for ad in net:
    k += 1
    if ad == ip_address('206.158.124.67'):
        print(ad, k)

a = int(net.network_address)
b = int(ip_address('206.158.124.67'))
print(b - a)