from ipaddress import *
net = ip_network('166.192.0.0/255.252.0.0', 0)

cnt = 0
for ad in net:
    ad2 = f'{ad:b}'
    if ad2.count('1') % 2 != 0:
        cnt += 1
print(cnt)
