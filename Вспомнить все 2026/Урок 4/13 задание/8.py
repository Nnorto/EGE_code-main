from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'166.174.84.182/{mask}', 0)
    if str(net.network_address) == '166.174.84.0':
        print(net.num_addresses)