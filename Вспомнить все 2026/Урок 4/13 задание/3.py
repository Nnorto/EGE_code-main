from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'155.99.138.55/{mask}', 0)
    if str(net.network_address) == '155.99.128.0':
        print(mask)