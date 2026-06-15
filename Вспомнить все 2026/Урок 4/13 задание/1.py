from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'147.132.56.124/{mask}', 0)
    if str(net.network_address) == '147.132.48.0':
        print(net.netmask)