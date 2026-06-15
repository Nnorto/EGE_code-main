from ipaddress import *
net = ip_network('0.0.0.0/255.255.252.0', 0)
cnt = 0
for ad in net:
    cnt += 1
print(cnt-2)

print(net.num_addresses-2)