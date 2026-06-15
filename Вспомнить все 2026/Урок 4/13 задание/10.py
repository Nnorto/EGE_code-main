from ipaddress import *
net = ip_network('214.181.62.141/255.255.255.240', 0)

cnt = 0
for ad in net:
    ad2 = f'{ad:b}'
    if ad2.count('1') % 4 != 0:
        cnt += 1
print(cnt)
