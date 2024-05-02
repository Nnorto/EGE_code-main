from ipaddress import *
net = ip_network('0.0.0.0/255.255.255.128', 0)
c = 0
for ad in net:
    c += 1
print(c)

# или

print(net.num_addresses)