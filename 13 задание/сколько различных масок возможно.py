from ipaddress import *
c = 0
for mask in range(0, 33):
    net = ip_network('93.138.164.49/' + str(mask), 0)
    if net.network_address == ip_address('93.138.160.0'):
        c += 1
print(c)




