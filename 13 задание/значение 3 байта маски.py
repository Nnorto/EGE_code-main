from ipaddress import *
for mask in range(32, -1, -1):
    net1 = ip_network(f'211.188.211.49/{mask}', 0)
    net2 = ip_network(f'211.188.200.115/{mask}', 0)
    if net1.network_address != net2.network_address:
        print(net1.netmask)

