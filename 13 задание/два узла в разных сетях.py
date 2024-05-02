from ipaddress import *

for mask in range(0, 33):
    net1 = ip_network('84.77.95.123/' + str(mask), 0)
    net2 = ip_network('84.77.96.123/' + str(mask), 0)
    if net1.network_address != net2.network_address:
        print(mask, net1.netmask)




