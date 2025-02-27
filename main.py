from ipaddress import *
for mask in range(33):
    net = ip_network(f'188.162.71.183/{mask}', 0)
    if net.network_address == ip_address('188.162.71.128'):
        print(net.num_addresses)

