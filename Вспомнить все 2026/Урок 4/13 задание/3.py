from ipaddress import *
cnt = 0
for mask in range(32+1):
    net = ip_network(f'211.193.32.53/{mask}', 0)
    if str(net.network_address) == '211.193.32.0':
        cnt += 1

print(cnt)