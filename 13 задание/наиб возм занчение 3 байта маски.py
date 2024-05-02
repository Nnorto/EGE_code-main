from ipaddress import *

for mask in range(0, 33):
    net = ip_network('111.81.200.27/' + str(mask), 0)
    if net.network_address == ip_address('111.81.192.0'):
        print(mask, net.netmask)




