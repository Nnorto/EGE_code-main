from ipaddress import *
net = ip_network('202.71.92.91/255.255.192.0', 0)

for ad in net:
    ad2 = f'{ad:b}'
    oktet = [int(x) for x in str(ad).split('.')]
    nch = [x for x in oktet if x % 2 != 0]
    if len(nch) == 2:
        print(ad)



